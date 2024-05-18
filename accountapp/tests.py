from django.test import TestCase

# Create your tests here.
# manager_info/tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import sensor

class SensorTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sensor_data = {
            'temperature': 25.5,
            'humidity': 60.0,
            'dust': 10.2
        }
        self.response = self.client.post(reverse('sensor-list'), self.sensor_data, format='json')

    def test_api_can_create_sensor_data(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_sensor_data(self):
        response = self.client.get(reverse('sensor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
