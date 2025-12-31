def get_active_items(prescription):
    return prescription.items.filter(
        is_active=True,
        status="active"
    ).order_by("created_at")
