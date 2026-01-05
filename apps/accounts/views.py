from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from common.constants import UserRole

from django.contrib.auth.decorators import login_required
from common.permissions import role_required

# Create your views here.
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )

        if user:
            login(request, user)
            return home_redirect(request)

        messages.error(request, "Invalid credentials")

    return render(request, "auth/login.html")



def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def home_redirect(request):
    role = request.user.role

    if role == UserRole.RECEPTIONIST:
        return redirect("receptionist_dashboard")

    if role == UserRole.DOCTOR:
        return redirect("doctor_queue")

    if role == UserRole.MEDICAL_STAFF:
        return redirect("pharmacy_dashboard")

    if role == UserRole.HOSPITAL_ADMIN:
        return redirect("hospital_admin_dashboard")

    return redirect("login")


@login_required
@role_required(UserRole.HOSPITAL_ADMIN)
def hospital_admin_dashboard(request):
    return render(
    request,
    "hospital_admin/staff_dashboard.html",
    {
        "sidebar_template": "base/sidebar/hospital_admin.html"
    }
)

