from django.urls import path
from .views import DoctorQueueAPI, ReceptionistQueueAPI

urlpatterns = [
    path("doctor-queue/", DoctorQueueAPI.as_view()),
    path("receptionist-queue/", ReceptionistQueueAPI.as_view()),
]
