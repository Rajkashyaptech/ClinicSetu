from django.core.exceptions import PermissionDenied
from common.constants import UserRole


def can_access_visit(user, visit):
    if user.role == UserRole.DOCTOR:
        if visit.doctor != user:
            raise PermissionDenied("Not your consultation")

    if user.role in (
        UserRole.RECEPTIONIST,
        UserRole.MEDICAL_STAFF,
        UserRole.HOSPITAL_ADMIN,
    ):
        if visit.hospital != user.hospital:
            raise PermissionDenied("Invalid hospital")

    return True
