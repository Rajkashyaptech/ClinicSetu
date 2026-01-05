from datetime import timedelta
from django.utils.timezone import now
from django.db.models import Max

from apps.visits.models import Visit
from common.constants import UserRole


def get_consultation_history(*, user):
    qs = (
        Visit.objects
        .filter(
            hospital=user.hospital,
            prescription__isnull=False,
        )
        # 🔑 IMPORTANT PART
        .annotate(
            last_session_completed_at=Max(
                "sessions__completed_at"
            )
        )
        .filter(
            last_session_completed_at__isnull=False
        )
        .select_related(
            "patient",
            "doctor",
        )
        .prefetch_related(
            "sessions",
            "sessions__prescription_items",
        )
        # 🔑 ORDER BY LAST SESSION, NOT VISIT
        .order_by("-last_session_completed_at")
    )

    # Doctor → only own consultations
    if user.role == UserRole.DOCTOR:
        qs = qs.filter(doctor=user)

    # Non-admins → last 30 days based on SESSION time
    if user.role != UserRole.HOSPITAL_ADMIN:
        qs = qs.filter(
            last_session_completed_at__gte=now() - timedelta(days=30)
        )

    return qs
