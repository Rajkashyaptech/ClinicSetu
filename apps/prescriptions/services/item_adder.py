from ..models import PrescriptionItem


def add_prescription_item(*, prescription, session, medicine_name, dosage, frequency, duration):
    return PrescriptionItem.objects.create(
        prescription=prescription,
        session=session,
        medicine_name=medicine_name,
        dosage=dosage,
        frequency=frequency,
        duration=duration,
        status=PrescriptionItem.STATUS_ACTIVE
    )
