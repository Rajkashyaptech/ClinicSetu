from django.db import transaction
from django.utils import timezone
from ..models import Visit, PatientVitals
from apps.consultations.models import ConsultationSession
from apps.consultations.services.followup_creator import create_followup_session
from apps.audit.services.logger import log_action


ALLOWED_VITAL_FIELDS = {
    "height_cm",
    "weight_kg",
    "pulse_rate",
    "temperature_c",
    "blood_pressure",
}


@transaction.atomic
def create_visit_with_vitals(*, hospital, patient, doctor, vitals_data):
    """
    Create new visit OR create follow-up session if visit already exists
    """

    # 🔍 1. Check for active visit
    visit = (
        Visit.objects
        .filter(
            hospital=hospital,
            patient=patient,
            doctor=doctor,
            is_active=True,
        )
        .order_by("-created_at")
        .first()
    )

    # 🔁 FOLLOW-UP FLOW
    if visit and not visit.is_expired():
        session = create_followup_session(visit)
        return visit, session

    # 🆕 NEW VISIT FLOW
    visit = Visit.objects.create(
        hospital=hospital,
        patient=patient,
        doctor=doctor,
    )

    filtered_vitals = {
        key: value
        for key, value in vitals_data.items()
        if key in ALLOWED_VITAL_FIELDS and value is not None
    }

    if filtered_vitals:
        PatientVitals.objects.create(
            visit=visit,
            **filtered_vitals
        )

    session = ConsultationSession.objects.create(
        visit=visit,
        doctor=doctor,
        session_number=1,
        status=ConsultationSession.STATUS_OPEN,
        started_at=timezone.now(),
    )

    log_action(
        actor=None,  # receptionist
        action="VISIT_CREATED",
        entity="Visit",
        entity_id=visit.id,
        metadata={
            "patient_id": patient.id,
            "doctor_id": doctor.id,
            "hospital_id": hospital.id
        }
    )

    return visit, session
