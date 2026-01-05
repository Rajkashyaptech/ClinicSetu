from apps.prescriptions.models import Prescription


def get_or_create_prescription(*, visit, session):
    """
    One prescription per visit.
    Can be used across multiple sessions.
    """

    prescription, _ = Prescription.objects.get_or_create(
        visit=visit
    )

    return prescription
