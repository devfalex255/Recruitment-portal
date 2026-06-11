from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "email",
        "role",

    ]

    search_fields = ["email"]



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        "primary_key",
        "unique_id",
        "user",
        "phone",
        "address",
    ]

    search_fields = ["phone", "address"]


