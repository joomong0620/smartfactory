from rest_framework import serializers
from .models import manager_info, production, sensor, ovensensor


class managerSerializer(serializers.ModelSerializer):
    class Meta:
        model = manager_info
        fields = \
            '__all__'

class productionSerializer(serializers.ModelSerializer):
    class Meta:
        model = production
        fields = \
            '__all__'

class sensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensor
        fields = \
            '__all__'


class ovensensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ovensensor
        fields = \
            '__all__'

