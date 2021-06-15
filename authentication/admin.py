from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import Uzer

# Register your models here.
admin.site.register(Uzer, UserAdmin)