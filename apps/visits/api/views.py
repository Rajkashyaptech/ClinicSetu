from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from common.api_permissions import IsReceptionist
from apps.patients.models import Patient
from apps.accounts.models import User
from apps.visits.services.visit_creator import create_visit_with_vitals
from .serializers import VisitCreateSerializer


class CreateVisitAPI(APIView):
    permission_classes = [IsReceptionist]

    def post(self, request):
        serializer = VisitCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        patient = Patient.objects.get(
            id=serializer.validated_data["patient_id"],
            hospital=request.user.hospital
        )

        doctor = User.objects.get(
            id=serializer.validated_data["doctor_id"],
            hospital=request.user.hospital
        )

        vitals_data = {
            key: serializer.validated_data[key]
            for key in ("height_cm", "weight_kg", "pulse_rate")
            if key in serializer.validated_data
        }

        visit = create_visit_with_vitals(
            hospital=request.user.hospital,
            patient=patient,
            doctor=doctor,
            vitals_data=vitals_data
        )

        return Response(
            {"visit_id": visit.id},
            status=status.HTTP_201_CREATED
        )
