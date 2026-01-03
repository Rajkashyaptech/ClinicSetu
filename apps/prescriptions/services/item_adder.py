from ..models import PrescriptionItem

from apps.audit.services.logger import log_action
from apps.medicines.services.learner import learn_medicine


def add_prescription_item(*, prescription, session, medicine_name, dosage, frequency, duration):
    item = PrescriptionItem.objects.create(
        prescription=prescription,
        session=session,
        medicine_name=medicine_name,
        dosage=dosage,
        frequency=frequency,
        duration=duration,
        status=PrescriptionItem.STATUS_ACTIVE
    )

    learn_medicine(medicine_name)

    log_action(
        actor=session.doctor,
        action="MEDICINE_ADDED",
        entity="Prescription",
        entity_id=prescription.id,
        metadata={
            "medicine": medicine_name,
            "session_id": session.id
        }
    )

    return item
