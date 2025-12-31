from django.db import models
from apps.visits.models import Visit
from apps.consultations.models import ConsultationSession

# Create your models here.
class Prescription(models.Model):
    visit = models.OneToOneField(
        Visit,
        on_delete=models.CASCADE,
        related_name="prescription"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for Visit {self.visit.id}"
    


class PrescriptionItem(models.Model):
    STATUS_ACTIVE = "active"
    STATUS_STOPPED = "stopped"

    STATUS_CHOICES = [
        (STATUS_ACTIVE, "Active"),
        (STATUS_STOPPED, "Stopped"),
    ]

    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        related_name="items"
    )

    session = models.ForeignKey(
        ConsultationSession,
        on_delete=models.CASCADE,
        related_name="prescription_items"
    )

    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_at"]
