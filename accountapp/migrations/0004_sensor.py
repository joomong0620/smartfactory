# Generated by Django 5.0.4 on 2024-05-07 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0003_alter_manager_info_manager_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='sensor',
            fields=[
                ('data_id', models.IntegerField(primary_key=True, serialize=False)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('finedust', models.DecimalField(decimal_places=2, max_digits=5)),
                ('manager_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.manager_info')),
            ],
        ),
    ]
