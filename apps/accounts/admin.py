from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('role',)
    fieldsets = (
        (None, {'fields': ('role', 'image',)}),
    ) + UserAdmin.fieldsets
