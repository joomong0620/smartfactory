from django.contrib import admin
from .models import manager_info, production, sensor, ovensensor
admin.site.register(manager_info)
admin.site.register(production)
admin.site.register(sensor)
admin.site.register(ovensensor)
# Register your models here.
