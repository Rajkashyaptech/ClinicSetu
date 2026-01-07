from apps.pharmacy.models import DispenseRecord
from apps.consultations.models import ConsultationSession

def get_or_create_dispense_record(session: ConsultationSession):
    record, _ = DispenseRecord.objects.get_or_create(
        session=session
    )
    return record
