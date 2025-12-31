from apps.consultations.models import ConsultationSession


def get_pharmacy_queue(hospital):
    return (
        ConsultationSession.objects
        .select_related(
            "visit",
            "visit__patient",
            "visit__prescription"
        )
        .filter(
            visit__hospital=hospital,
            status=ConsultationSession.STATUS_COMPLETED
        )
        .order_by("-completed_at")
    )
