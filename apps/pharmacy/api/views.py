from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from common.api_permissions import IsMedicalStaff

from apps.pharmacy.services.dispense_initializer import get_or_create_dispense_record
from apps.pharmacy.services.print_marker import mark_as_printed
from apps.pharmacy.services.dispense_marker import mark_as_dispensed

from apps.prescriptions.models import Prescription
from apps.consultations.models import ConsultationSession
from apps.pharmacy.models import DispenseRecord


class MarkPrintedAPI(APIView):
    permission_classes = [IsMedicalStaff]

    def post(self, request, record_id):
        prescription = Prescription.objects.get(
            id=record_id,
            visit__hospital=request.user.hospital
        )

        if not prescription.visit.sessions.filter(
            status=ConsultationSession.STATUS_COMPLETED
        ).exists():
            raise ValidationError("Consultation not completed yet")

        record = get_or_create_dispense_record(prescription)
        mark_as_printed(record)

        return Response({"status": "printed"})


class MarkDispensedAPI(APIView):
    permission_classes = [IsMedicalStaff]

    def post(self, request, record_id):
        prescription = Prescription.objects.get(
            id=record_id,
            visit__hospital=request.user.hospital
        )

        if not prescription.visit.sessions.filter(
            status=ConsultationSession.STATUS_COMPLETED
        ).exists():
            raise ValidationError("Consultation not completed yet")

        record = get_or_create_dispense_record(prescription)
        mark_as_dispensed(record)

        return Response({"status": "dispensed"})


class PharmacyQueueAPI(APIView):
    permission_classes = [IsMedicalStaff]

    def get(self, request):
        records = DispenseRecord.objects.filter(
            prescription__visit__hospital=request.user.hospital,
            prescription__visit__sessions__status=ConsultationSession.STATUS_COMPLETED,
            is_dispensed=False
        ).select_related(
            "prescription",
            "prescription__visit",
            "prescription__visit__patient",
            "prescription__visit__doctor"
        ).order_by(
            "prescription__visit__sessions__completed_at"
        )

        data = []

        for r in records:
            visit = r.prescription.visit
            completed_session = visit.sessions.filter(
                status=ConsultationSession.STATUS_COMPLETED
            ).first()

            data.append({
                "prescription_id": r.prescription.id,
                "patient_name": visit.patient.full_name,
                "doctor_name": visit.doctor.username,
                "completed_at": (
                    completed_session.completed_at.isoformat()
                    if completed_session and completed_session.completed_at
                    else None
                ),
            })

        return Response(data)
