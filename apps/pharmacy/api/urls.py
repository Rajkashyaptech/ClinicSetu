from django.urls import path
from .views import MarkPrintedAPI, MarkDispensedAPI
from .views import PharmacyQueueAPI

urlpatterns = [
    path("queue/", PharmacyQueueAPI.as_view(), name="pharmacy-queue"),
    path("print/<int:record_id>/", MarkPrintedAPI.as_view(), name="mark-printed"),
    path("dispense/<int:record_id>/", MarkDispensedAPI.as_view(), name="mark-dispensed"),
]
