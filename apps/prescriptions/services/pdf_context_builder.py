from django.utils.timezone import localtime


def build_consultation_pdf_context(*, visit):
    hospital = visit.hospital
    patient = visit.patient
    doctor = visit.doctor

    sessions = visit.sessions.prefetch_related(
        "prescription_items"
    ).order_by("session_number")

    context = {
        # Hospital Branding
        "hospital": {
            "name": hospital.name,
            "address": hospital.address,
            "phone": hospital.phone,
            "footer_note": hospital.footer_note,
            "logo_url": hospital.logo.url if hospital.logo else None,
        },

        # Patient Info
        "patient": {
            "full_name": patient.full_name,
            "age": patient.age,
            "gender": patient.gender,
            "phone": patient.phone_number,
        },

        # Doctor Info
        "doctor": {
            "name": doctor.username,
        },

        # Visit Info
        "visit": {
            "visit_date": localtime(visit.created_at),
            "validity_days": visit.validity_days,
        },

        # Sessions (ONE PAGE PER SESSION)
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
                    for item in session.prescription_items.all()
                ],
            }
            for session in sessions
            if session.completed_at  # only completed sessions
        ],

        # Meta
        "generated_at": localtime(),
    }

    return context
