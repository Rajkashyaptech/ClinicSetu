from apps.visits.models import Visit

def get_active_visit(patient, doctor, hospital):
    visit = Visit.objects.filter(
        patient=patient,
        doctor=doctor,
        hospital=hospital,
        is_active=True,
    ).order_by("-created_at").first()

    if visit and not visit.is_expired():
        return visit

    return None
