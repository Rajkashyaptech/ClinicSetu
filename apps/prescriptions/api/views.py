from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from common.api_permissions import IsDoctor
from apps.consultations.models import ConsultationSession
from apps.prescriptions.services.prescription_creator import (
    get_or_create_prescription
)
from apps.prescriptions.models import PrescriptionItem
from apps.prescriptions.services.item_adder import add_prescription_item
from apps.prescriptions.services.item_remover import remove_prescription_item


class AddMedicineAPI(APIView):
    permission_classes = [IsDoctor]

    def post(self, request):
        session = ConsultationSession.objects.get(
            id=request.data["session_id"],
            doctor=request.user,
            visit__hospital=request.user.hospital
        )

        prescription = get_or_create_prescription(
            visit=session.visit,
            session=session
        )

        add_prescription_item(
            prescription=prescription,
            session=session,
            medicine_name=request.data["medicine"],
            dosage=request.data["dosage"],
            frequency=request.data["frequency"],
            duration=request.data["duration"],
        )

        return Response(
            {"status": "added"},
            status=status.HTTP_201_CREATED
        )


class RemoveMedicineAPI(APIView):
    permission_classes = [IsDoctor]

    def post(self, request):
        item = PrescriptionItem.objects.get(
            id=request.data["item_id"],
            prescription__visit__hospital=request.user.hospital
        )

        session = ConsultationSession.objects.get(
            id=request.data["session_id"],
            doctor=request.user
        )

        remove_prescription_item(item, session)
        return Response({"status": "removed"})


class ActivePrescriptionItemsAPI(APIView):
    permission_classes = [IsDoctor]

    def get(self, request):
        prescription_id = request.query_params.get("prescription_id")
        session_id = request.query_params.get("session_id")

        items = PrescriptionItem.objects.filter(
            prescription_id=prescription_id,
            session_id=session_id,
            status="active",
            prescription__visit__hospital=request.user.hospital
        ).values(
            "id",
            "medicine_name",
            "dosage",
            "frequency",
            "duration",
            "session_id"
        )

        return Response(list(items))
