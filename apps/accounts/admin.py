from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    ordering = ("id",)
    list_display = ("username", "role", "hospital", "is_active")
    list_filter = ("role", "hospital", "is_active")
    search_fields = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("hospital", "role")}),
        (_("Permissions"), {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        (_("Important dates"), {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "role", "hospital"),
        }),
    )

    readonly_fields = ("last_login",)
