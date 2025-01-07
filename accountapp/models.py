from django.db import models


class manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    com_name = models.CharField(max_length=50)
    reg_time = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # 사진 경로

class production(models.Model):
    production_id = models.AutoField(primary_key=True)
    manager_pro_fk = models.ForeignKey('manager', on_delete=models.CASCADE)
    day_production = models.CharField(max_length=50, null=True)
    day_defects = models.CharField(max_length=50, null=True)
    Month_production = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class sensor(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pm10 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pm25 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)


class ovensensor(models.Model):
    oven_id = models.AutoField(primary_key=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    #image = models.ImageField(upload_to="image")


class HandDetection(models.Model):
    hand_detected = models.BooleanField(default=False)  # 손 감지 여부 (True: 감지됨, False: 감지되지 않음)
    timestamp = models.DateTimeField(auto_now_add=True)  # 데이터가 생성된 시간

class web(models.Model):
    hand_detected = models.BooleanField(default=False)  # 손 감지 여부 (True: 감지됨, False: 감지되지 않음)
    timestamp = models.DateTimeField(auto_now_add=True)  # 데이터가 생성된 시간

