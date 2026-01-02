from django.db import transaction
from ..models import Visit, PatientVitals
from apps.consultations.models import ConsultationSession

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
    visit = Visit.objects.create(
        hospital=hospital,
        patient=patient,
        doctor=doctor
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

    ConsultationSession.objects.create(
        visit=visit,
        doctor=doctor,
        session_number=1
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

    return visit
