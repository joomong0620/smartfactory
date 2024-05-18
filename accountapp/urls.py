from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'manager', views.manageViewSet, basename='manager')
router.register(r'product', views.prodViewSet, basename='product')
router.register(r'sensor', views.sensorViewSet, basename='sensor')

urlpatterns = [
    path('', include(router.urls)),

]
