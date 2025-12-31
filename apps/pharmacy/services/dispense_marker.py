from django.utils.timezone import now


def mark_as_dispensed(dispense_record):
    if dispense_record.is_dispensed:
        return dispense_record

    dispense_record.is_dispensed = True
    dispense_record.dispensed_at = now()
    dispense_record.save(
        update_fields=["is_dispensed", "dispensed_at"]
    )
    return dispense_record
