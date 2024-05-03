from django.urls import include, path, re_path

from .views import RedirectView, ReturnView

event_patterns = [
    re_path(
        r"^ogone/",
        include(
            [
                path(
                    "redirect/<str:order>/<str:hash>/<str:payment>/",
                    RedirectView.as_view(),
                    name="redirect",
                ),
                path(
                    "return/<str:order>/<str:hash>/<str:payment>/<str:result>/",
                    ReturnView.as_view(),
                    name="return",
                ),
            ]
        ),
    ),
]
