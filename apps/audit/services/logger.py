from apps.audit.models import AuditLog


def log_action(*, hospital, user, action, entity_type, entity_id, metadata=None):
    AuditLog.objects.create(
        hospital=hospital,
        user=user,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        metadata=metadata or {}
    )
