from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from common.permissions import role_required
from common.constants import UserRole

from apps.prescriptions.services.item_adder import add_prescription_item

# Create your views here.
@login_required
@role_required(UserRole.DOCTOR)
def add_medicine(request, prescription_id):
    if request.method == "POST":
        add_prescription_item(
            prescription_id=prescription_id,
            session_id=request.POST["session_id"],
            medicine_name=request.POST["medicine"],
            dosage=request.POST["dosage"],
            frequency=request.POST["frequency"],
            duration=request.POST["duration"]
        )

    return redirect("consultation_detail")
