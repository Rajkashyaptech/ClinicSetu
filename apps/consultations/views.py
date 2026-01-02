from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from common.permissions import role_required
from common.constants import UserRole

from apps.consultations.services.doctor_queue import get_doctor_queue
from apps.consultations.services.session_closer import complete_session

from apps.consultations.models import ConsultationSession
from apps.prescriptions.models import Prescription

from apps.consultations.services.patient_history import get_recent_visit_history


# Create your views here.
@login_required
@role_required(UserRole.DOCTOR)
def doctor_queue(request):
    sessions = get_doctor_queue(request.user)
    return render(
        request,
        "consultations/doctor_queue.html",
        {"sessions": sessions}
    )


@login_required
@role_required(UserRole.DOCTOR)
def complete_consultation(request, session_id):
    session = get_object_or_404(
        ConsultationSession,
        id=session_id,
        doctor=request.user,
        visit__hospital=request.user.hospital
    )

    complete_session(session)
    return redirect("doctor_queue")


@login_required
@role_required(UserRole.DOCTOR)
def doctor_dashboard(request):
    return render(request, "doctor/queue.html")


@login_required
@role_required(UserRole.DOCTOR)
def consultation_detail(request, session_id):
    session = get_object_or_404(
        ConsultationSession,
        id=session_id,
        doctor=request.user,
        visit__hospital=request.user.hospital
    )

    prescription, _ = Prescription.objects.get_or_create(
        visit=session.visit
    )

    items = prescription.items.filter(status="active")

    patient = session.visit.patient
    history = get_recent_visit_history(
        patient=patient,
        exclude_visit=session.visit
    )

    return render(
        request,
        "doctor/consultation.html",
        {
            "session": session,
            "prescription": prescription,
            "items": items,
            "history": history,
        }
    )


@login_required
@role_required(UserRole.DOCTOR)
def complete_consultation(request, session_id):
    session = get_object_or_404(
        ConsultationSession,
        id=session_id,
        doctor=request.user,
        visit__hospital=request.user.hospital
    )

    complete_session(session)
    return redirect("doctor_dashboard")
