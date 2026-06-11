from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        "primary_key",
        "unique_id",
        "title",
        "description",
        "posted_by",
        "created_at",
        "is_active",
    ]

    search_fields = ["title"]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = [
        "primary_key",
        "unique_id",
        "job",
        "applicant",
        "status",
        "created_at",
        "is_active",
    ]

    search_fields = ["status"]
