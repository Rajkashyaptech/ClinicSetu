from django.contrib import admin
from .models import Hospital

# Register your models here.
@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    search_fields = ("name",)

    fieldsets = (
        ("Basic Info", {
            "fields": ("name", "is_active")
        }),
        ("Branding", {
            "fields": ("logo", "address", "phone", "footer_note")
        }),
        ("SaaS Limits", {
            "fields": (
                "max_doctors",
                "max_receptionists",
                "max_medical_staff",
            )
        }),
    )
