from django.core.exceptions import PermissionDenied

def remove_prescription_item(item, session):
    # Allow removal only during the same session
    if item.session_id != session.id:
        raise PermissionDenied("Cannot remove past session medicine")

    if session.status != session.STATUS_OPEN:
        raise PermissionDenied("Session already completed")

    item.is_active = False
    item.save(update_fields=["is_active"])
