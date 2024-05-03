import hashlib
from binascii import hexlify
from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _  # NoQA
from django.views import View
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from pretix.base.models import Order, OrderPayment, Quota
from pretix.base.payment import PaymentException
from pretix.multidomain.urlreverse import eventreverse

from pretix_ogone.constants import SHA_OUT_PARAMETERS


class OgoneOrderView:
    def dispatch(self, request, *args, **kwargs):
        try:
            self.order = request.event.orders.get(code=kwargs["order"])
            if (
                hashlib.sha1(self.order.secret.lower().encode()).hexdigest()
                != kwargs["hash"].lower()
            ):
                raise Http404("Unknown order")
        except Order.DoesNotExist:
            # Do a hash comparison as well to harden timing attacks
            if (
                "abcdefghijklmnopq".lower()
                == hashlib.sha1("abcdefghijklmnopq".encode()).hexdigest()
            ):
                raise Http404("Unknown order")
            else:
                raise Http404("Unknown order")
        return super().dispatch(request, *args, **kwargs)

    @cached_property
    def pprov(self):
        return self.payment.payment_provider

    @property
    def payment(self):
        return get_object_or_404(
            self.order.payments,
            pk=self.kwargs["payment"],
            provider__istartswith="ogone",
        )


@method_decorator(xframe_options_exempt, "dispatch")
class RedirectView(OgoneOrderView, TemplateView):
    template_name = "pretix_ogone/redirecting.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["url"] = self.pprov.settings.backend + "orderstandard_utf8.asp"
        ctx["params"] = self.pprov.sign_parameters(
            self.pprov.params_for_payment(self.payment, self.request),
        )
        return ctx


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(xframe_options_exempt, "dispatch")
class ReturnView(OgoneOrderView, View):
    def get(self, request, *args, **kwargs):
        return self._handle(request.GET)

    def post(self, request, *args, **kwargs):
        return self._handle(request.POST)

    def _handle(self, data):
        if not self.validate_digest(data, self.pprov):
            messages.error(
                self.request,
                _(
                    "Sorry, we could not validate the payment result. Please try again or "
                    "contact the event organizer to check if your payment was successful."
                ),
            )
            return self._redirect_to_order()

        if self.kwargs.get("result") == "cancel":
            self.payment.fail(
                info_data=dict(data.items()),
                log_data={"result": self.kwargs.get("result"), **dict(data.items())},
            )
            return self._redirect_to_order()
        elif self.kwargs.get("result") in ("decline", "exception"):
            self.payment.fail(
                info_data=dict(data.items()),
                log_data={"result": self.kwargs.get("result"), **dict(data.items())},
            )
            messages.error(
                self.request,
                _("The payment has failed. You can click below to try again."),
            )
            return self._redirect_to_order()
        elif self.kwargs.get("result") == "accept":
            try:
                self.process_result(data, self.payment, self.pprov)
            except Quota.QuotaExceededException as e:
                messages.error(self.request, str(e))

            return self._redirect_to_order()
        else:
            self.payment.fail(
                info_data=dict(data.items()),
                log_data={"result": self.kwargs.get("result"), **dict(data.items())},
            )
            messages.error(
                self.request,
                _("The payment has failed. You can click below to try again."),
            )

        return self._redirect_to_order()

    def _redirect_to_order(self):
        return redirect(
            eventreverse(
                self.request.event,
                "presale:event.order",
                kwargs={"order": self.order.code, "secret": self.order.secret},
            )
            + ("?paid=yes" if self.order.status == Order.STATUS_PAID else "")
        )

    def validate_digest(self, data, prov):
        if "SHASIGN" in data:
            data = {k.upper(): v for k, v in data.items()}
            digest_in = data["SHASIGN"]
            digest = hashlib.sha512()
            for parname in SHA_OUT_PARAMETERS:
                if parname in data and data[parname]:
                    digest.update(
                        f"{parname}={data[parname]}{prov.settings.sha_out_pass}".encode()
                    )
            return digest.hexdigest().upper() == digest_in.upper()
        return False

    def process_result(self, data, payment, prov):
        payment.info_data = data
        payment.save(update_fields=["info"])
        if data["STATUS"] == "5":
            try:
                prov.capture_payment(payment)
            except PaymentException as e:
                messages.error(
                    self.request,
                    _("The payment has failed. You can click below to try again."),
                )
                self.payment.fail(log_data={"exception": str(e)})
        elif data["STATUS"] == "9":
            self.payment.confirm()
        else:
            messages.error(
                self.request,
                _("The payment has failed. You can click below to try again."),
            )
            self.payment.fail(
                info_data=dict(data.items()),
                log_data={"result": self.kwargs.get("result"), **dict(data.items())},
            )
