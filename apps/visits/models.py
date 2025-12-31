from django.db import models
from django.utils.timezone import timedelta, now, localdate
from apps.hospitals.models import Hospital
from apps.patients.models import Patient
from apps.accounts.models import User


# Create your models here.
class Visit(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    validity_days = models.PositiveIntegerField(default=7)

    is_active = models.BooleanField(default=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def validity_end_date(self):
        return self.created_at.date() + timedelta(days=self.validity_days)

    def is_expired(self):
        return localdate() > self.validity_end_date()

    def close(self):
        if not self.is_active:
            return
        self.is_active = False
        self.closed_at = now()
        self.save(update_fields=["is_active", "closed_at"])


class PatientVitals(models.Model):
    visit = models.OneToOneField(
        Visit,
        on_delete=models.CASCADE,
        related_name="vitals"
    )

    height_cm = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    weight_kg = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    blood_pressure = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    pulse_rate = models.PositiveIntegerField(null=True, blank=True)

    temperature_c = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True
    )

    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vitals for Visit {self.visit.id}"
