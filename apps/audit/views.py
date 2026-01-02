from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.audit.models import AuditLog
from common.permissions import role_required
from common.constants import UserRole

# Create your views here.
@login_required
@role_required(UserRole.SUPER_ADMIN, UserRole.HOSPITAL_ADMIN)
def audit_log_view(request):
    user = request.user

    logs = AuditLog.objects.select_related("actor").order_by("-created_at")

    # Hospital admin sees only their hospital logs
    if user.role == UserRole.HOSPITAL_ADMIN:
        logs = logs.filter(actor__hospital=user.hospital)

    return render(
        request,
        "audit/audit_log_list.html",
        {"logs": logs[:500]}  # hard limit for safety
    )
