from ..models import PrescriptionItem

from apps.audit.services.logger import log_action


def stop_prescription_item(*, prescription, session, medicine_name):
    item = PrescriptionItem.objects.create(
        prescription=prescription,
        session=session,
        medicine_name=medicine_name,
        dosage="",
        frequency="",
        duration="",
        status=PrescriptionItem.STATUS_STOPPED
    )

    log_action(
        actor=session.doctor,
        action="MEDICINE_STOPPED",
        entity="Prescription",
        entity_id=prescription.id,
        metadata={
            "medicine": medicine_name,
            "session_id": session.id
        }
    )

    return item
