from django.utils.timezone import now

from apps.consultations.models import ConsultationSession
from apps.pharmacy.services.dispense_initializer import (
    get_or_create_dispense_record
)

from apps.audit.services.logger import log_action


def create_new_session(*, visit, doctor):
    """
    Create a new consultation session for a visit.
    Session number increments per visit.
    """

    last_session = (
        ConsultationSession.objects
        .filter(visit=visit)
        .order_by("-session_number")
        .first()
    )

    next_session_number = (
        last_session.session_number + 1
        if last_session
        else 1
    )

    return ConsultationSession.objects.create(
        visit=visit,
        doctor=doctor,
        session_number=next_session_number,
        status=ConsultationSession.STATUS_OPEN
    )


def complete_session(session):
    if session.status == session.STATUS_COMPLETED:
        return session

    # Complete session
    session.status = session.STATUS_COMPLETED
    session.completed_at = now()
    session.save(update_fields=["status", "completed_at"])

    # CLOSE VISIT
    visit = session.visit
    if visit.is_active:
        visit.is_active = False
        visit.closed_at = now()
        visit.save(update_fields=["is_active", "closed_at"])

    # Audit log
    log_action(
        actor=session.doctor,
        action="SESSION_COMPLETED",
        entity="ConsultationSession",
        entity_id=session.id,
        metadata={
            "visit_id": visit.id,
            "session_number": session.session_number
        }
    )

    # Initialize pharmacy workflow (once per visit)
    if hasattr(visit, "prescription"):
        get_or_create_dispense_record(visit.prescription)

    return session
