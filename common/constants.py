class UserRole:
    SUPER_ADMIN = "super_admin"
    HOSPITAL_ADMIN = "hospital_admin"
    DOCTOR = "doctor"
    RECEPTIONIST = "receptionist"
    MEDICAL_STAFF = "medical_staff"

    CHOICES = [
        (SUPER_ADMIN, "Super Admin"),
        (HOSPITAL_ADMIN, "Hospital Admin"),
        (DOCTOR, "Doctor"),
        (RECEPTIONIST, "Receptionist"),
        (MEDICAL_STAFF, "Medical Staff"),
    ]
