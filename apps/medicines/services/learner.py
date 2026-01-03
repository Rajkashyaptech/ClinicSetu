from apps.medicines.models import Medicine


def learn_medicine(name: str):
    """
    Silently store medicine name if not already known.
    Never raises errors.
    """
    if not name:
        return
    
    normalized = name.strip().title()

    Medicine.objects.get_or_create(name=normalized)
