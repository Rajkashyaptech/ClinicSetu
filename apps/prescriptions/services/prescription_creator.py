from ..models import Prescription


def get_or_create_prescription(visit, session):
    if session.session_number != 1:
        raise ValueError("Prescription can only be created in first session")

    prescription, _ = Prescription.objects.get_or_create(
        visit=visit
    )
    return prescription
