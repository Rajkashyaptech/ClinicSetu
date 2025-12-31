from django.db import models
from apps.hospitals.models import Hospital

# Create your models here.
class Patient(models.Model):
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name="patients"
    )

    full_name = models.CharField(max_length=255)
    age = models.PositiveBigIntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        null=True,
        blank=True
    )

    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.phone_number})"
