from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from common.permissions import role_required
from common.constants import UserRole

from apps.consultations.services.doctor_queue import get_doctor_queue
from apps.consultations.services.session_closer import complete_session

from apps.consultations.models import ConsultationSession
from apps.prescriptions.models import Prescription

from apps.consultations.services.patient_history import get_recent_visit_history

from apps.consultations.services.history import (
    get_consultation_history
)
from apps.visits.models import Visit
from apps.consultations.services.history_permissions import (
    can_access_visit
)
from apps.prescriptions.services.pdf_context_builder import (
    build_consultation_pdf_context
)
from apps.prescriptions.services.pdf_generator import (
    generate_consultation_pdf
)


# Create your views here.
@login_required
@role_required(UserRole.DOCTOR)
def doctor_queue(request):
    sessions = get_doctor_queue(request.user)
    return render(
        request,
        "doctor/queue.html",
        {
            "sessions": sessions,
            "sidebar_template": "base/sidebar/doctor.html",
        }
    )


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

    # Medicines added in THIS session only
    current_items = prescription.items.filter(
        session=session,
        status="active"
    )

    # Medicines from PREVIOUS sessions (history)
    previous_items = prescription.items.exclude(
        session=session
    )


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
            "current_items": current_items,
            "previous_items": previous_items,
            "history": history,
            "sidebar_template": "base/sidebar/doctor.html",
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
    return redirect("doctor_queue")


@login_required
@role_required(
    UserRole.DOCTOR,
    UserRole.RECEPTIONIST,
    UserRole.MEDICAL_STAFF,
    UserRole.HOSPITAL_ADMIN,
)
def consultation_history(request):
    visits = get_consultation_history(user=request.user)

    sidebar_map = {
        UserRole.DOCTOR: "base/sidebar/doctor.html",
        UserRole.RECEPTIONIST: "base/sidebar/receptionist.html",
        UserRole.MEDICAL_STAFF: "base/sidebar/pharmacy.html",
        UserRole.HOSPITAL_ADMIN: "base/sidebar/hospital_admin.html",
    }

    return render(
        request,
        "history/consultation_list.html",
        {
            "visits": visits,
            "sidebar_template": sidebar_map.get(request.user.role),
        }
    )


@login_required
def consultation_view(request, visit_id):
    visit = get_object_or_404(
        Visit,
        id=visit_id,
        prescription__isnull=False
    )

    can_access_visit(request.user, visit)

    return render(
        request,
        "history/consultation_view.html",
        {
            "visit": visit,
            "sidebar_template": {
                UserRole.DOCTOR: "base/sidebar/doctor.html",
                UserRole.RECEPTIONIST: "base/sidebar/receptionist.html",
                UserRole.MEDICAL_STAFF: "base/sidebar/pharmacy.html",
                UserRole.HOSPITAL_ADMIN: "base/sidebar/hospital_admin.html",
            }.get(request.user.role),
        }
    )


@login_required
@role_required(
    UserRole.DOCTOR,
    UserRole.RECEPTIONIST,
    UserRole.MEDICAL_STAFF,
    UserRole.HOSPITAL_ADMIN,
)
def consultation_pdf(request, visit_id):
    visit = get_object_or_404(
        Visit,
        id=visit_id,
        prescription__isnull=False
    )

    can_access_visit(request.user, visit)

    context = build_consultation_pdf_context(visit=visit)
    return generate_consultation_pdf(context=context)
