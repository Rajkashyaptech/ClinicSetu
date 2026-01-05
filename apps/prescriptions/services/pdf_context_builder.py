from django.utils.timezone import localtime

from apps.prescriptions.models import PrescriptionItem


def build_consultation_pdf_context(*, visit):
    hospital = visit.hospital
    patient = visit.patient
    doctor = visit.doctor

    sessions = (
        visit.sessions
        .prefetch_related("prescription_items")
        .order_by("session_number")
    )

    return {
        "hospital": {
            "name": hospital.name,
            "address": hospital.address,
            "phone": hospital.phone,
            "footer_note": hospital.footer_note,
            "logo_path": hospital.logo.path if hospital.logo else None,
        },
        "patient": {
            "full_name": patient.full_name,
            "age": patient.age,
            "gender": patient.gender,
            "phone": patient.phone_number,
        },
        "doctor": {
            "name": doctor.username,
        },
        "visit": {
            "visit_date": localtime(visit.created_at),
            "validity_days": visit.validity_days,
        },
        "sessions": [
            {
                "session_number": s.session_number,
                "date": localtime(s.completed_at),
                "medicines": [
                    {
                        "name": item.medicine_name,
                        "dosage": item.dosage,
                        "frequency": item.frequency,
                        "duration": item.duration,
                        "status": item.status,
                    }
                    for item in s.prescription_items.all()
                ],
            }
            for s in sessions if s.completed_at
        ],
        "generated_at": localtime(),
    }


def build_session_pdf_context(*, session):
    visit = session.visit
    hospital = visit.hospital
    patient = visit.patient
    doctor = session.doctor

    items = PrescriptionItem.objects.filter(
        session=session
    ).order_by("created_at")

    return {
        "hospital": {
            "name": hospital.name,
            "address": hospital.address,
            "phone": hospital.phone,
            "footer_note": hospital.footer_note,
            "logo_path": hospital.logo.path if hospital.logo else None,
        },

        "patient": {
            "full_name": patient.full_name,
            "age": patient.age,
            "gender": patient.gender,
            "phone": patient.phone_number,
        },

        "doctor": {
            "name": doctor.username,
        },

        "visit": {
            "visit_date": localtime(visit.created_at),
            "validity_days": visit.validity_days,
        },

        "sessions": [
            {
                "session_number": session.session_number,
                "date": localtime(session.completed_at),
                "medicines": [
                    {
                        "name": item.medicine_name,
                        "dosage": item.dosage,
                        "frequency": item.frequency,
                        "duration": item.duration,
                        "status": item.status,
                    }
                    for item in items
                ],
            }
        ],

        "generated_at": localtime(),
    }
