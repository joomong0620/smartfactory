from django.contrib import admin
from .models import manager_info, production, sensor
admin.site.register(manager_info)
admin.site.register(production)
admin.site.register(sensor)
# Register your models here.
