from django.urls import path
from .views import DoctorQueueAPI, ReceptionistQueueAPI

urlpatterns = [
    path(
        "doctor/queue/",
        DoctorQueueAPI.as_view(),
        name="doctor_queue_api",
    ),
    path("receptionist-queue/", ReceptionistQueueAPI.as_view()),
]
