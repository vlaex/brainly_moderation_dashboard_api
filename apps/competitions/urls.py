from django.urls import path
from .views import ListCompetitionsView


urlpatterns = [
    path("", ListCompetitionsView.as_view(), name="competitions-list"),
]
