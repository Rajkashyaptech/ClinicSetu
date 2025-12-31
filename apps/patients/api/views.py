from rest_framework.views import APIView
from rest_framework.response import Response

from common.api_permissions import IsReceptionist
from apps.patients.models import Patient
from .serializers import PatientSerializer


class PatientLookupAPI(APIView):
    permission_classes = [IsReceptionist]

    def get(self, request):
        phone = request.query_params.get("phone")
        qs = Patient.objects.filter(
            hospital=request.user.hospital,
            phone_number=phone
        )
        return Response(PatientSerializer(qs, many=True).data)


class PatientCreateOrGetAPI(APIView):
    permission_classes = [IsReceptionist]

    def post(self, request):
        phone = request.data["phone"]

        patient_id = request.data.get("patient_id")

        # Case 1: Existing patient selected
        if patient_id:
            patient = Patient.objects.get(
                id=patient_id,
                hospital=request.user.hospital
            )
            return Response({
                "id": patient.id,
                "full_name": patient.full_name,
                "is_new": False
            })

        # Case 2: New patient (even if phone exists)
        patient = Patient.objects.create(
            hospital=request.user.hospital,
            phone_number=phone,
            full_name=request.data["full_name"],
            age=request.data.get("age"),
            gender=request.data.get("gender"),
        )

        return Response({
            "id": patient.id,
            "full_name": patient.full_name,
            "is_new": True
        })
