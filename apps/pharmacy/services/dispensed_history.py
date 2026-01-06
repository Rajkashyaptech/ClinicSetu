from django.utils.timezone import now, timedelta
from apps.pharmacy.models import DispenseRecord


def get_dispensed_history(user, days=30):
    return (
        DispenseRecord.objects
        .filter(
            prescription__visit__hospital=user.hospital,
            is_dispensed=True,
            dispensed_at__gte=now() - timedelta(days=days)
        )
        .select_related(
            "prescription",
            "prescription__visit",
            "prescription__visit__patient",
            "prescription__visit__doctor",
        )
        .order_by("-dispensed_at")
    )
