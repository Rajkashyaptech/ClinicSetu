from django.core.management.base import BaseCommand
from django.utils.timezone import now
from apps.visits.models import Visit


class Command(BaseCommand):
    help = "Close expired visits"

    def handle(self, *args, **kwargs):
        expired_visits = Visit.objects.filter(
            is_active=True
        )

        count = 0
        for visit in expired_visits:
            if visit.is_expired():
                visit.close()
                count += 1

        self.stdout.write(
            self.style.SUCCESS(f"Closed {count} expired visits")
        )
