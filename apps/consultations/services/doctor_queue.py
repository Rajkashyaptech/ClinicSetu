from ..models import ConsultationSession

def get_doctor_queue(doctor):
    return (
        ConsultationSession.objects
        .select_related("visit", "visit__patient")
        .filter(
            doctor=doctor,
            status=ConsultationSession.STATUS_OPEN,
            visit__hospital=doctor.hospital,
            visit__is_active=True
        )
        .order_by("started_at")
    )
