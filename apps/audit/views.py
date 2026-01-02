from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.audit.models import AuditLog
from common.constants import UserRole

# Create your views here.
@login_required
def audit_log_view(request):
    user = request.user

    if user.role == UserRole.SUPER_ADMIN:
        logs = AuditLog.objects.select_related("actor").order_by("-created_at")

    elif user.role == UserRole.HOSPITAL_ADMIN:
        logs = AuditLog.objects.select_related("actor").filter(
            actor__hospital=user.hospital
        ).order_by("-created_at")

    else:
        return render(request, "403.html", status=403)

    return render(
        request,
        "audit/audit_log_list.html",
        {"logs": logs[:500]}  # hard limit for safety
    )
