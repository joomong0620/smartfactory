from django.contrib import admin
from .models import manager, production, sensor, ovensensor, post, HandDetection

admin.site.register(manager)
admin.site.register(production)
admin.site.register(sensor)
admin.site.register(ovensensor)
admin.site.register(post)
admin.site.register(HandDetection)
# Register your models here.
