from apps.audit.models import AuditLog


def log_action(*, actor, action, entity, entity_id, metadata=None):
    AuditLog.objects.create(
        actor=actor,
        action=action,
        entity=entity,
        entity_id=str(entity_id),
        metadata=metadata or {}
    )
