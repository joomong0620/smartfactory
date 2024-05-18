from django.db import models
import uuid
from datetime import datetime


class manager_info(models.Model):
    manager_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    com_name = models.CharField(max_length=50)
    reg_time = models.DateTimeField(auto_now_add=True)
    log_time = models.DateTimeField(auto_now=True)

class production(models.Model):
    production_id = models.IntegerField(primary_key=True)
    manager_pro_fk = models.ForeignKey('manager_info', on_delete=models.CASCADE)
    day_production = models.CharField(max_length=50, null=True)
    day_defects = models.CharField(max_length=50, null=True)
    Month_production = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class sensor(models.Model):
    sensor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    dust = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

