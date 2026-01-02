from apps.visits.models import Visit
from apps.prescriptions.models import PrescriptionItem


def get_recent_visit_history(*, patient, exclude_visit, limit=3):
    visits = (
        Visit.objects
        .filter(patient=patient)
        .exclude(id=exclude_visit.id)
        .order_by("-created_at")[:limit]
    )

    history = []

    for visit in visits:
        items = PrescriptionItem.objects.filter(
            prescription__visit=visit
        ).values(
            "medicine_name",
            "dosage",
            "frequency",
            "duration",
            "status"
        )

        history.append({
            "visit_date": visit.created_at,
            "doctor": visit.doctor.username,
            "medicines": list(items),
        })

    return history
