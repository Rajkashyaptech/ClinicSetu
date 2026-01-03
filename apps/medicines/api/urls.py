from django.urls import path
from .views import MedicineAutocompleteAPI


urlpatterns = [
    path("autocomplete/", MedicineAutocompleteAPI.as_view()),
]
