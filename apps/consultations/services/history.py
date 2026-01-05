from datetime import timedelta
from django.utils.timezone import now

from apps.visits.models import Visit
from common.constants import UserRole


def get_consultation_history(*, user):
    qs = (
        Visit.objects.filter(
            hospital=user.hospital,
            prescription__isnull=False,
        )
        .select_related("patient", "doctor")
        .prefetch_related(
            "sessions",
            "sessions__prescription_items",
        )
        .order_by("-created_at")
    )

    if user.role == UserRole.DOCTOR:
        qs = qs.filter(doctor=user)

    if user.role != UserRole.HOSPITAL_ADMIN:
        qs = qs.filter(
            created_at__gte=now() - timedelta(days=30)
        )

    return qs
