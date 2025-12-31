from ..models import DispenseRecord


def get_or_create_dispense_record(prescription):
    record, _ = DispenseRecord.objects.get_or_create(
        prescription=prescription
    )
    return record
