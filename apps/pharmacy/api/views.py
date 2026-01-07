from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from common.api_permissions import IsMedicalStaff

from apps.pharmacy.services.dispense_initializer import get_or_create_dispense_record
from apps.pharmacy.services.print_marker import mark_as_printed
from apps.pharmacy.services.dispense_marker import mark_as_dispensed

from apps.consultations.models import ConsultationSession
from apps.pharmacy.models import DispenseRecord


class MarkPrintedAPI(APIView):
    permission_classes = [IsMedicalStaff]

    def post(self, request, session_id):
        session = ConsultationSession.objects.get(
            id=session_id,
            visit__hospital=request.user.hospital,
            status=ConsultationSession.STATUS_COMPLETED
        )

        record = get_or_create_dispense_record(session)
        mark_as_printed(record)

        return Response({"status": "printed"})


class MarkDispensedAPI(APIView):
    permission_classes = [IsMedicalStaff]

    def post(self, request, session_id):
        session = ConsultationSession.objects.get(
            id=session_id,
            visit__hospital=request.user.hospital,
            status=ConsultationSession.STATUS_COMPLETED
        )

        record = get_or_create_dispense_record(session)
        mark_as_dispensed(record)

        return Response({"status": "dispensed"})


class PharmacyQueueAPI(APIView):
    permission_classes = [IsMedicalStaff]

    def get(self, request):
        records = (
            DispenseRecord.objects
            .filter(
                session__visit__hospital=request.user.hospital,
                is_dispensed=False,
                session__status=ConsultationSession.STATUS_COMPLETED,
            )
            .select_related(
                "session",
                "session__visit",
                "session__visit__patient",
                "session__visit__doctor",
                "session__visit__prescription",
            )
            .order_by("-session__completed_at")
        )

        data = []

        for r in records:
            visit = r.session.visit
            prescription = visit.prescription

            data.append({
                "prescription_id": prescription.id,
                "patient_name": visit.patient.full_name,
                "doctor_name": visit.doctor.username,
                "completed_at": (
                    r.session.completed_at.isoformat()
                    if r.session.completed_at else None
                ),
            })

        return Response(data)
