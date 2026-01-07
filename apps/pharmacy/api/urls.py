from django.urls import path
from .views import MarkPrintedAPI, MarkDispensedAPI, PharmacyQueueAPI

urlpatterns = [
    path("queue/", PharmacyQueueAPI.as_view(), name="pharmacy-queue"),

    # SESSION-BASED
    path("print/<int:session_id>/", MarkPrintedAPI.as_view(), name="mark-printed"),
    path("dispense/<int:session_id>/", MarkDispensedAPI.as_view(), name="mark-dispensed"),
]
