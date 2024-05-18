# Generated by Django 5.0.4 on 2024-05-07 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='manager_info',
            fields=[
                ('manager_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('com_name', models.CharField(max_length=50)),
                ('reg_time', models.DateTimeField(auto_now_add=True)),
                ('log_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='production',
            fields=[
                ('production_id', models.IntegerField(primary_key=True, serialize=False)),
                ('day_production', models.CharField(max_length=50)),
                ('day_defects', models.CharField(max_length=50)),
                ('Month_production', models.CharField(max_length=50)),
                ('manager_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.manager_info')),
            ],
        ),
    ]
