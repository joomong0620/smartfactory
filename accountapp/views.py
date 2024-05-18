from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def manage_post(request):
    if request.method == 'POST':
        # 새로운 데이터를 생성하는 로직 추가 (여기에 필요한 내용을 작성하세요)
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
    'patch': 'p[partial_update',
    'delete': 'destroy',
})

@api_view(['POST'])
def prod_post(request):
    if request.method == 'POST':
        # 새로운 데이터를 생성하는 로직 추가 (여기에 필요한 내용을 작성하세요)
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
    'patch': 'p[partial_update',
    'delete': 'destroy',
})

@api_view(['POST'])
def sensor_post(request):
    if request.method == 'POST':
        # 새로운 데이터를 생성하는 로직 추가 (여기에 필요한 내용을 작성하세요)
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
    'patch': 'p[partial_update',
    'delete': 'destroy',
})

