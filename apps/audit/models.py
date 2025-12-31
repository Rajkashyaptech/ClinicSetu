from django.db import models
from apps.accounts.models import User
from apps.hospitals.models import Hospital

# Create your models here.
class AuditLog(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True
    )

    action = models.CharField(max_length=255)
    entity_type = models.CharField(max_length=100)
    entity_id = models.PositiveIntegerField()

    metadata = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} on {self.entity_type}:{self.entity_id}"
