from django.utils.timezone import now


def mark_as_printed(dispense_record):
    if dispense_record.is_printed:
        return dispense_record

    dispense_record.is_printed = True
    dispense_record.printed_at = now()
    dispense_record.save(
        update_fields=["is_printed", "printed_at"]
    )
    return dispense_record
