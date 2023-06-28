from django.contrib import admin
from core.models import EmailNotification
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class EmailNotificationAdmin(admin.StackedInline):
    model = EmailNotification
    can_delete = False
    verbose_name_plural = 'Email Notifications'

class CustomizedUserAdmin (UserAdmin):
    inlines = (EmailNotificationAdmin,)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)