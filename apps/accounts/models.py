from django.db import models
from django.contrib.auth.models import AbstractUser

from common.constants import UserRole
from apps.hospitals.models import Hospital

# Create your models here.
class User(AbstractUser):
    role = models.CharField(
        max_length=30,
        choices=UserRole.CHOICES
    )

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="users"
    )

    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ["role"]

    def is_super_admin(self):
        return self.role == UserRole.SUPER_ADMIN

    def is_doctor(self):
        return self.role == UserRole.DOCTOR

    def __str__(self):
        return f"{self.username} ({self.role})"
