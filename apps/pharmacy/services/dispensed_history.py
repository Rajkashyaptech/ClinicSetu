from apps.pharmacy.models import DispenseRecord
from apps.consultations.models import ConsultationSession


def get_dispensed_history(user):
    """
    Returns dispensed consultation sessions for medical staff
    """

    return (
        DispenseRecord.objects
        .filter(
            session__visit__hospital=user.hospital,
            is_dispensed=True,
            session__status=ConsultationSession.STATUS_COMPLETED,
        )
        .select_related(
            "session",
            "session__visit",
            "session__visit__patient",
            "session__visit__doctor",
        )
        .order_by("-dispensed_at")
    )
