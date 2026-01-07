from datetime import timedelta
from django.utils.timezone import now

from apps.consultations.models import ConsultationSession
from common.constants import UserRole


def get_consultation_history(*, user):
    """
    DOCTOR / STAFF CONSULTATION HISTORY
    One row = one completed consultation session
    """

    qs = (
        ConsultationSession.objects
        .filter(
            visit__hospital=user.hospital,
            status=ConsultationSession.STATUS_COMPLETED,
        )
        .select_related(
            "visit",
            "visit__patient",
            "visit__doctor",
        )
        .order_by("-completed_at")
    )

    # Doctor → only own sessions
    if user.role == UserRole.DOCTOR:
        qs = qs.filter(doctor=user)

    # Non-admin → last 30 days (based on session time)
    if user.role != UserRole.HOSPITAL_ADMIN:
        qs = qs.filter(
            completed_at__gte=now() - timedelta(days=30)
        )

    return qs
