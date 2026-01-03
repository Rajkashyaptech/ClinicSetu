from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    # SaaS limits
    max_doctors = models.PositiveIntegerField(default=0)
    max_receptionists = models.PositiveIntegerField(default=0)
    max_medical_staff = models.PositiveIntegerField(default=0)

    # 🧾 Branding (NEW)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    footer_note = models.CharField(
        max_length=255,
        blank=True,
        help_text="Shown at bottom of consultation PDF"
    )
    logo = models.ImageField(
        upload_to="hospital_logos/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
