from django.db import transaction
from django.utils import timezone
from apps.consultations.models import ConsultationSession


@transaction.atomic
def create_followup_session(visit):
    visit.refresh_from_db()

    if not visit.is_active:
        raise ValueError("Visit is closed")

    if visit.is_expired():
        visit.close()
        raise ValueError("Visit validity expired")

    last_session = visit.sessions.order_by("-session_number").first()

    if last_session and last_session.status != ConsultationSession.STATUS_COMPLETED:
        raise ValueError("Previous session still open")
    
    return ConsultationSession.objects.create(
        visit=visit,
        doctor=visit.doctor,
        session_number=last_session.session_number + 1,
        status=ConsultationSession.STATUS_OPEN,
        started_at=timezone.now(),
    )
