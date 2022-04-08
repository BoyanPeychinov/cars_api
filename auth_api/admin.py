from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth_api.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'first_name', 'last_name', 'age', 'phone_number', 'user_image')
    list_filter = ('is_staff', 'is_superuser', 'groups', 'first_name', 'last_name', 'age')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'age', 'phone_number', 'user_image',)}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'created_at', 'deleted_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'age', 'phone_number', 'user_image'),
        }),
    )

    readonly_fields = ('created_at', 'last_login', 'deleted_at')
