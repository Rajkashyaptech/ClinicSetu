from django.urls import path
from .views import CreateVisitAPI

urlpatterns = [
    path("create/", CreateVisitAPI.as_view(), name="visit-create"),
]
