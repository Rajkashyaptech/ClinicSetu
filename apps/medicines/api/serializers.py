from rest_framework import serializers
from apps.medicines.models import Medicine


class MedicineAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ("id", "name")
