from datetime import timedelta
from django.utils.timezone import now

from apps.visits.models import Visit
from common.constants import UserRole


def get_consultation_history(*, user):
    """
    Returns queryset of visits eligible for history view.
    Read-only, finalized consultations only.
    """

    qs = Visit.objects.filter(
        hospital=user.hospital,
        prescription__isnull=False,
        is_active=False,  # visit closed
    ).select_related(
        "patient", "doctor"
    ).order_by("-created_at")

    # Doctor: only own consultations
    if user.role == UserRole.DOCTOR:
        qs = qs.filter(doctor=user)

    # Non-admins: last 30 days
    if user.role != UserRole.HOSPITAL_ADMIN:
        qs = qs.filter(
            created_at__gte=now() - timedelta(days=30)
        )

    return qs
