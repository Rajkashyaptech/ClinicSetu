from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    # SaaS limits
    max_doctors = models.PositiveIntegerField(default=5)
    max_receptionists = models.PositiveIntegerField(default=1)
    max_medical_staff = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
