from apps.pharmacy.models import DispenseRecord

def get_pharmacy_queue(user):
    return (
        DispenseRecord.objects
        .select_related(
            "session",
            "session__visit",
            "session__visit__patient",
            "session__visit__doctor",
        )
        .filter(
            session__visit__hospital=user.hospital,
            is_dispensed=False,
        )
        .order_by("created_at")
    )
