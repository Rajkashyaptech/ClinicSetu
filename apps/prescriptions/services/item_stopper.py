from ..models import PrescriptionItem


def stop_prescription_item(*, prescription, session, medicine_name):
    return PrescriptionItem.objects.create(
        prescription=prescription,
        session=session,
        medicine_name=medicine_name,
        dosage="",
        frequency="",
        duration="",
        status=PrescriptionItem.STATUS_STOPPED
    )
