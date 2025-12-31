from django.urls import path
from .views import (
    DoctorListAPI,
    StaffListAPI,
    CreateStaffAPI,
    UpdateStaffAPI,
    UpdateStaffStatusAPI,
)

urlpatterns = [
    path("doctors/", DoctorListAPI.as_view()),

    path("staff/", StaffListAPI.as_view()),
    path("staff/create/", CreateStaffAPI.as_view()),
    path("staff/update/<int:user_id>/", UpdateStaffAPI.as_view()),
    path("staff/status/<int:user_id>/", UpdateStaffStatusAPI.as_view()),
]
