from rest_framework import serializers
from apps.patients.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "full_name",
            "age",
            "gender",
            "phone_number",
            "address",
        ]
