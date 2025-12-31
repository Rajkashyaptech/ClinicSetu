from django.urls import path
from .views import ActivePrescriptionItemsAPI, AddMedicineAPI, RemoveMedicineAPI

urlpatterns = [
    path("active/", ActivePrescriptionItemsAPI.as_view(), name="active-medicines"),
    path("add-medicine/", AddMedicineAPI.as_view(), name="add-medicine"),
    path("remove-medicine/", RemoveMedicineAPI.as_view(), name="remove-medicine"),
]
