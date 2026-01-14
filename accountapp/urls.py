from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    check_email, login_view,
    manageViewSet, prodViewSet, sensorViewSet, ovensensorViewSet, postViewSet, hand_detection, get_hand_detection,
    process_image, update_profile, hand_detection2, web_hand)

router = DefaultRouter()
router.register(r'manager', manageViewSet, basename='manager')
router.register(r'product', prodViewSet, basename='product')
router.register(r'sensor', sensorViewSet, basename='sensor')
router.register(r'ovensensor', ovensensorViewSet, basename='ovensensor')
router.register(r'post', postViewSet, basename='post')

urlpatterns = [
    path('check_email/', check_email, name='check_email'),
    path('process/', process_image, name='process_image'),  # URL 등록
    path('login/', login_view, name='login'),
    path('hand_detection/', hand_detection, name='hand_detection'),
    path('hand_detection2/', hand_detection2, name='hand_detection'),
    path('get_hand_detection/', get_hand_detection, name='get_hand_detection'),
    path('web_hand/', web_hand, name='web_hand'),
    path('profile_update/', update_profile, name='profile_update'),
    path('', include(router.urls)),
]

