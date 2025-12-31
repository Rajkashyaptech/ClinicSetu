from rest_framework import serializers
from apps.consultations.models import ConsultationSession


class DoctorQueueSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(
        source="visit.patient.full_name"
    )

    class Meta:
        model = ConsultationSession
        fields = [
            "id",
            "session_number",
            "patient_name",
            "started_at",
        ]
