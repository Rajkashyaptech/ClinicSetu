from django.urls import path
from .views import PatientLookupAPI, PatientCreateOrGetAPI

urlpatterns = [
    path("lookup/", PatientLookupAPI.as_view(), name="patient-lookup"),
    path("create-or-get/", PatientCreateOrGetAPI.as_view()),
]
