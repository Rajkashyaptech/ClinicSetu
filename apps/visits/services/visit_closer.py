from django.utils.timezone import now
from apps.audit.services.logger import log_action

def close_visit(*, visit, actor=None):
    if not visit.is_active:
        return visit

    visit.is_active = False
    visit.closed_at = now()
    visit.save(update_fields=["is_active", "closed_at"])

    log_action(
        actor=actor,
        action="VISIT_CLOSED",
        entity="Visit",
        entity_id=visit.id,
    )

    return visit
