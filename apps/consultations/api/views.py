from rest_framework.views import APIView
from rest_framework.response import Response

from common.api_permissions import IsDoctor, IsReceptionist
from apps.consultations.services.doctor_queue import get_doctor_queue
from .serializers import DoctorQueueSerializer

from apps.consultations.models import ConsultationSession

class DoctorQueueAPI(APIView):
    permission_classes = [IsDoctor]

    def get(self, request):
        sessions = get_doctor_queue(request.user)
        return Response(
            DoctorQueueSerializer(sessions, many=True).data
        )


class ReceptionistQueueAPI(APIView):
    permission_classes = [IsReceptionist]

    def get(self, request):
        sessions = ConsultationSession.objects.filter(
            visit__hospital=request.user.hospital,
            status=ConsultationSession.STATUS_OPEN
        ).select_related(
            "visit__patient",
            "doctor"
        ).order_by("started_at")   # ✅ correct field

        queue = {}

        for session in sessions:
            doctor_name = session.doctor.username
            queue.setdefault(doctor_name, []).append({
                "patient_name": session.visit.patient.full_name,
                "started_at": session.started_at,
            })

        return Response(queue)
