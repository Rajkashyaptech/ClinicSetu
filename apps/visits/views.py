from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from common.permissions import role_required
from common.constants import UserRole

from apps.patients.models import Patient
from apps.visits.services.visit_creator import create_visit_with_vitals

# Create your views here.
@login_required
@role_required(UserRole.RECEPTIONIST)
def create_visit(request):
    if request.method == "POST":
        patient_id = request.POST.get("patient_id")
        doctor_id = request.POST.get("doctor_id")

        vitals_data = {
            "height_cm": request.POST.get("height_cm") or None,
            "weight_kg": request.POST.get("weight_kg") or None,
            "pulse_rate": request.POST.get("pulse_rate") or None,
        }

        patient = Patient.objects.get(
            id=patient_id,
            hospital=request.user.hospital
        )

        visit, session = create_visit_with_vitals(
            hospital=request.user.hospital,
            patient=patient,
            doctor_id=doctor_id,
            vitals_data=vitals_data
        )

        return redirect("receptionist_dashboard")

    return render(request, "visits/create_visit.html")


@login_required
@role_required(UserRole.RECEPTIONIST)
def receptionist_dashboard(request):
    return render(
    request,
    "receptionist/create_visit.html",
    {
        "sidebar_template": "base/sidebar/receptionist.html"
    }
)

