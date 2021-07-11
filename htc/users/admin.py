from django.contrib.auth.admin import UserAdmin as UA
from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(UA):
    list_display = ("email", "first", "last", "phone", "rating", "bio", "date_joined", "last_login", "is_admin", "is_staff")
    search_fields = ("email", "first", "last")
    readonly_fields = ("date_joined", "last_login")
    ordering = ("email", )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)
