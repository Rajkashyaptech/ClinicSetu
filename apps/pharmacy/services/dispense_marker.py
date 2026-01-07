from django.utils.timezone import now
from apps.audit.services.logger import log_action


def mark_as_dispensed(record):
    if record.is_dispensed:
        return record

    record.is_dispensed = True
    record.dispensed_at = now()
    record.save(update_fields=["is_dispensed", "dispensed_at"])

    log_action(
        actor=None,  # medical staff
        action="MEDICINE_DISPENSED",
        entity="ConsultationSession",
        entity_id=record.session.id,
        metadata={
            "session_number": record.session.session_number,
            "visit_id": record.session.visit.id,
        }
    )

    return record
