from django.urls import path
from .views import doctor_dashboard, consultation_detail, complete_consultation

urlpatterns = [
    path("doctor/", doctor_dashboard, name="doctor_dashboard"),
    path("consult/<int:session_id>/", consultation_detail, name="consultation_detail"),
    path(
        "consult/<int:session_id>/complete/",
        complete_consultation,
        name="complete_consultation"
    ),
]
