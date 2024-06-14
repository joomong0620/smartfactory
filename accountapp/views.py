from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import manager_info, production, sensor, ovensensor
from .serializer import managerSerializer, productionSerializer, sensorSerializer, ovensensorSerializer
import torch
from PIL import Image


@api_view(['POST'])
def manage_post(request):
    if request.method == 'POST':
        pass

class manageViewSet(viewsets.ModelViewSet):
    queryset = manager_info.objects.all()
    serializer_class = managerSerializer

manage_list = manageViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
manage_detail = manageViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

@api_view(['POST'])
def prod_post(request):
    if request.method == 'POST':
        pass

class prodViewSet(viewsets.ModelViewSet):
    queryset = production.objects.all()
    serializer_class = productionSerializer

prod_list = prodViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
prod_detail = prodViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

@api_view(['POST'])
def sensor_post(request):
    if request.method == 'POST':
        pass

class sensorViewSet(viewsets.ModelViewSet):
    queryset = sensor.objects.all()
    serializer_class = sensorSerializer

sensor_list = sensorViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
sensor_detail = sensorViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

@api_view(['POST'])
def ovensensor_post(request):
    if request.method == 'POST':
        pass

class ovensensorViewSet(viewsets.ModelViewSet):
    queryset = ovensensor.objects.all()
    serializer_class = ovensensorSerializer

ovensensor_list = ovensensorViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
ovensensor_detail = ovensensorViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})