from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from common.api_permissions import IsReceptionist, IsHospitalAdmin
from common.constants import UserRole

from apps.accounts.models import User
from apps.accounts.services.staff_manager import (
    create_staff_user,
    set_staff_status,
    update_staff_details,
)


class DoctorListAPI(APIView):
    permission_classes = [IsReceptionist]

    def get(self, request):
        doctors = User.objects.filter(
            hospital=request.user.hospital,
            role=UserRole.DOCTOR,
            is_active=True
        )

        return Response([
            {"id": d.id, "name": d.username}
            for d in doctors
        ])


class StaffListAPI(APIView):
    permission_classes = [IsHospitalAdmin]

    def get(self, request):
        hospital = request.user.hospital

        staff_qs = User.objects.filter(
            hospital=hospital
        ).exclude(
            role=UserRole.HOSPITAL_ADMIN
        )

        return Response({
            "limits": {
                "doctors": hospital.max_doctors,
                "receptionists": hospital.max_receptionists,
                "medical_staff": hospital.max_medical_staff,
            },
            "usage": {
                "doctors": staff_qs.filter(role=UserRole.DOCTOR, is_active=True).count(),
                "receptionists": staff_qs.filter(role=UserRole.RECEPTIONIST, is_active=True).count(),
                "medical_staff": staff_qs.filter(role=UserRole.MEDICAL_STAFF, is_active=True).count(),
            },
            "staff": list(
                staff_qs.values("id", "username", "role", "is_active")
            )
        })


class CreateStaffAPI(APIView):
    permission_classes = [IsHospitalAdmin]

    def post(self, request):
        try:
            user = create_staff_user(
                hospital=request.user.hospital,
                username=request.data["username"],
                password=request.data["password"],
                role=request.data["role"]
            )
            return Response({"id": user.id}, status=201)

        except ValidationError as e:
            return Response({"error": str(e)}, status=400)


class UpdateStaffAPI(APIView):
    permission_classes = [IsHospitalAdmin]

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)

        try:
            update_staff_details(
                user=user,
                hospital=request.user.hospital,
                username=request.data.get("username"),
                password=request.data.get("password"),
            )
            return Response({"status": "updated"})

        except ValidationError as e:
            return Response({"error": str(e)}, status=400)


class UpdateStaffStatusAPI(APIView):
    permission_classes = [IsHospitalAdmin]

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)

        try:
            set_staff_status(
                user=user,
                hospital=request.user.hospital,
                is_active=request.data["is_active"]
            )
            return Response({"status": "updated"})

        except ValidationError as e:
            return Response({"error": str(e)}, status=400)

