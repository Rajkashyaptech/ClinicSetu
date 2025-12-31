from django.db import models
from apps.visits.models import Visit
from apps.accounts.models import User

# Create your models here.
class ConsultationSession(models.Model):
    STATUS_OPEN = "open"
    STATUS_COMPLETED = "completed"

    STATUS_CHOICES = [
        (STATUS_OPEN, "Open"),
        (STATUS_COMPLETED, "Completed"),
    ]

    visit = models.ForeignKey(
        Visit,
        on_delete=models.CASCADE,
        related_name="sessions"
    )

    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="consultation_sessions"
    )

    session_number = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_OPEN
    )

    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("visit", "session_number")
        ordering = ["started_at"]

    def __str__(self):
        return f"Visit {self.visit} - Session {self.session_number}"
