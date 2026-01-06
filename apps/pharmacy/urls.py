from django.urls import path
from .views import pharmacy_dashboard, prescription_detail, dispensed_history

urlpatterns = [
    path("", pharmacy_dashboard, name="pharmacy_dashboard"),
    path("prescription/<int:prescription_id>/", prescription_detail, name="pharmacy_prescription_detail"),

    path("", pharmacy_dashboard, name="pharmacy_dashboard"),
    path(
        "dispensed-history/",
        dispensed_history,
        name="pharmacy_dispensed_history"
    )

]
