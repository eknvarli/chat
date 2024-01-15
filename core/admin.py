from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import CustomUser, Script

# Register your models here.
@admin.register(CustomUser)
class CustomAdmin(UserAdmin):
    list_display = ('username','email')
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar Area', {
            'fields':['avatar']
        }),
    )

admin.site.register(Script)