from rest_framework import serializers
from .models import manager, production, sensor, ovensensor, post, HandDetection, web



class HandDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandDetection
        fields = \
            '__all__'

class webSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandDetection
        fields = \
            '__all__'
class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = post
        fields = ('title', 'text', 'image')


class RegisterSerializer(serializers.ModelSerializer):
        class Meta:
            model = manager
            fields = \
                '__all__'


class managerSerializer(serializers.ModelSerializer):
    class Meta:
        model = manager
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
