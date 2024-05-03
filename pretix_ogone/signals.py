import logging
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from pretix.base.settings import settings_hierarkey
from pretix.base.signals import logentry_display, register_payment_providers

logger = logging.getLogger(__name__)


@receiver(register_payment_providers, dispatch_uid="payment_ogone")
def register_payment_provider(sender, **kwargs):
    from .payment import OgoneCreditCard, OgoneSettingsHolder

    return [
        OgoneSettingsHolder,
        OgoneCreditCard,
    ]


@receiver(signal=logentry_display, dispatch_uid="ogone_logentry_display")
def pretixcontrol_logentry_display(sender, logentry, **kwargs):
    if not logentry.action_type.startswith("pretix_ogone.event"):
        return

    plains = {
        "canceled": _("Payment canceled."),
        "failed": _("Payment failed."),
        "paid": _("Payment succeeded."),
        "expired": _("Payment expired."),
        "disabled": _(
            "Payment method disabled since we were unable to refresh the access token. Please "
            "contact support."
        ),  # for historical reasons, no longer occurs
    }
    text = plains.get(logentry.action_type[20:], None)
    if text:
        return _("Ogone reported an event: {}").format(text)


settings_hierarkey.add_default("payment_ogone_method_cc", True, bool)
