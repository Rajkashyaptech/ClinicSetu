from django.core.exceptions import ValidationError
from apps.accounts.models import User
from common.constants import UserRole


def _active_count(hospital, role):
    return User.objects.filter(
        hospital=hospital,
        role=role,
        is_active=True
    ).count()


def can_create_staff(hospital, role):
    limits = {
        UserRole.DOCTOR: hospital.max_doctors,
        UserRole.RECEPTIONIST: hospital.max_receptionists,
        UserRole.MEDICAL_STAFF: hospital.max_medical_staff,
    }
    return _active_count(hospital, role) < limits.get(role, 0)


def create_staff_user(*, hospital, username, password, role):
    if role == UserRole.HOSPITAL_ADMIN:
        raise ValidationError("Cannot create hospital admin")

    if not can_create_staff(hospital, role):
        raise ValidationError(f"{role} limit reached")

    return User.objects.create_user(
        username=username,
        password=password,
        role=role,
        hospital=hospital
    )


def set_staff_status(*, user, hospital, is_active: bool):
    if user.hospital != hospital:
        raise ValidationError("Invalid hospital")

    if user.role == UserRole.HOSPITAL_ADMIN:
        raise ValidationError("Cannot modify hospital admin")

    user.is_active = is_active
    user.save(update_fields=["is_active"])


def update_staff_details(*, user, hospital, username=None, password=None):
    if user.hospital != hospital:
        raise ValidationError("Invalid hospital")

    if user.role == UserRole.HOSPITAL_ADMIN:
        raise ValidationError("Cannot modify hospital admin")

    if username:
        user.username = username

    if password:
        user.set_password(password)

    user.save()
