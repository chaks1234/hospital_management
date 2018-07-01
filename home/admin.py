from django.contrib import admin

# Register your models here.

from .models import Reg,Patient,Doctor

admin.site.register(Reg)
admin.site.register(Patient)
admin.site.register(Doctor)
