from rest_framework import serializers


class VisitCreateSerializer(serializers.Serializer):
    patient_id = serializers.IntegerField()
    doctor_id = serializers.IntegerField()

    height_cm = serializers.DecimalField(
        max_digits=5, decimal_places=2, required=False
    )
    weight_kg = serializers.DecimalField(
        max_digits=5, decimal_places=2, required=False
    )
    pulse_rate = serializers.IntegerField(required=False)
