from apps.consultations.models import ConsultationSession

def create_followup_session(visit):
    if not visit.is_active:
        raise ValueError("Visit is closed")

    if visit.is_expired():
        visit.close()
        raise ValueError("Visit validity expired")

    last_session = visit.sessions.order_by("-session_number").first()

    return ConsultationSession.objects.create(
        visit=visit,
        doctor=visit.doctor,
        session_number=last_session.session_number + 1
    )
