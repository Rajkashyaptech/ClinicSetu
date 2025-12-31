from django.http import HttpResponseForbidden
from common.constants import UserRole


def role_required(*allowed_roles):
    def decorator(view_func):
        def wrapped(request, *args, **kwargs):
            if request.user.role not in allowed_roles:
                return HttpResponseForbidden("You are not allowed")
            return view_func(request, *args, **kwargs)
        return wrapped
    return decorator
