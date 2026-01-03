from django.contrib import admin
from .models import Medicine

# Register your models here.
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
