from rest_framework.permissions import BasePermission
from common.constants import UserRole


class IsRole(BasePermission):
    allowed_roles = []

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role in self.allowed_roles
        )

class IsHospitalAdmin(IsRole):
    allowed_roles = ["hospital_admin"]


class IsReceptionist(IsRole):
    allowed_roles = [UserRole.RECEPTIONIST]


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == UserRole.DOCTOR
        )


class IsMedicalStaff(IsRole):
    allowed_roles = [UserRole.MEDICAL_STAFF]
