from django.utils.translation import gettext_lazy

from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    default = True
    name = "pretix_ogone"
    verbose_name = "Ogone"

    class PretixPluginMeta:
        name = gettext_lazy("Ogone")
        author = "pretix team"
        description = gettext_lazy(
            "Accept payments through the Ogone interface (legacy interface of Nexi Payengine / Wordline)"
        )
        visible = True
        version = __version__
        category = "PAYMENT"
        compatibility = "pretix>=2024.4.0"

    def ready(self):
        from . import signals  # NOQA
