from django.db import models
from apps.prescriptions.models import Prescription

# Create your models here.
class DispenseRecord(models.Model):
    session = models.OneToOneField(
        "consultations.ConsultationSession",
        on_delete=models.CASCADE,
        related_name="dispense_record"
    )

    is_printed = models.BooleanField(default=False)
    printed_at = models.DateTimeField(null=True, blank=True)

    is_dispensed = models.BooleanField(default=False)
    dispensed_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dispense for Session {self.session.id}"
