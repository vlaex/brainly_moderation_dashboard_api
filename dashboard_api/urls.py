from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/moderators", include("apps.moderators.urls")),
    path("api/v1/rankings", include("apps.rankings.urls")),
    path("api/v1/competitions", include("apps.competitions.urls"))
]


if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
