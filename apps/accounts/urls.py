# apps/accounts/urls.py
from django.urls import path
from .views import (
    login_view,
    logout_view,
    hospital_admin_dashboard,
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    path(
        "hospital-admin/",
        hospital_admin_dashboard,
        name="hospital_admin_dashboard"
    ),
]
