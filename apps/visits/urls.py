from django.urls import path
from .views import create_visit
from .views import receptionist_dashboard

urlpatterns = [
    path("create/", create_visit, name="create_visit"),

    path(
        "receptionist/",
        receptionist_dashboard,
        name="receptionist_dashboard"
    ),
]
