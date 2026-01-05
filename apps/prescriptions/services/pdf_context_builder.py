from django.utils.timezone import localtime


def build_consultation_pdf_context(*, visit):
    hospital = visit.hospital
    patient = visit.patient
    doctor = visit.doctor
    prescription = visit.prescription

    items = prescription.items.select_related(
        "session"
    ).order_by("id")

    context = {
        # 🏥 Hospital Branding
        "hospital": {
            "name": hospital.name,
            "address": hospital.address,
            "phone": hospital.phone,
            "footer_note": hospital.footer_note,
            "logo_url": hospital.logo.url if hospital.logo else None,
        },

        # 👤 Patient Info
        "patient": {
            "full_name": patient.full_name,
            "age": patient.age,
            "gender": patient.gender,
            "phone": patient.phone_number,
        },

        # 🩺 Doctor Info
        "doctor": {
            "name": doctor.username,
        },

        # 📅 Visit Info
        "visit": {
            "visit_date": localtime(visit.created_at),
            "validity_days": visit.validity_days,
        },

        # 💊 Medicines
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

        # 🕒 Meta
        "generated_at": localtime(),
    }

    return context
