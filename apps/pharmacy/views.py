from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from common.permissions import role_required
from common.constants import UserRole

from apps.pharmacy.services.print_marker import mark_as_printed
from apps.pharmacy.services.dispense_marker import mark_as_dispensed
from apps.pharmacy.models import DispenseRecord
from apps.prescriptions.models import Prescription
from apps.consultations.models import ConsultationSession

from apps.pharmacy.services.dispense_initializer import get_or_create_dispense_record
from apps.pharmacy.services.dispensed_history import get_dispensed_history

# Create your views here.

@login_required
@role_required(UserRole.MEDICAL_STAFF)
def mark_printed(request, record_id):
    record = DispenseRecord.objects.get(
        id=record_id,
        prescription__visit__hospital=request.user.hospital
    )
    mark_as_printed(record)
    return redirect("pharmacy_dashboard")


@login_required
@role_required(UserRole.MEDICAL_STAFF)
def mark_dispensed(request, record_id):
    record = DispenseRecord.objects.get(
        id=record_id,
        prescription__visit__hospital=request.user.hospital
    )
    mark_as_dispensed(record)
    return redirect("pharmacy_dashboard")


@login_required
@role_required(UserRole.MEDICAL_STAFF)
def pharmacy_dashboard(request):
    return render(
    request,
    "pharmacy/dashboard.html",
    {
        "sidebar_template": "base/sidebar/pharmacy.html"
    }
)



@login_required
@role_required(UserRole.MEDICAL_STAFF)
def prescription_detail(request, prescription_id):
    prescription = get_object_or_404(
        Prescription,
        id=prescription_id,
        visit__hospital=request.user.hospital
    )

    dispense_record = get_or_create_dispense_record(prescription)

    can_dispense = prescription.visit.sessions.filter(
        status=ConsultationSession.STATUS_COMPLETED
    ).exists()

    return render(
        request,
        "pharmacy/prescription_detail.html",
        {
            "prescription": prescription,
            "dispense_record": dispense_record,
            "can_dispense": can_dispense,
        }
    )


@login_required
@role_required(UserRole.MEDICAL_STAFF)
def dispensed_history(request):
    records = get_dispensed_history(request.user)
    return render(
        request,
        "pharmacy/dispensed_history.html",
        {
            "records": records,
            "sidebar_template": "base/sidebar/pharmacy.html",
        }
    )
