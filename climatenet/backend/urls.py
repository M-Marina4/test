from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views import DeviceDetailsViewSet

router = DefaultRouter()
router.register(r'devices', DeviceDetailsViewSet, basename='devices')

urlpatterns = [
    path('', include(router.urls)),
    path('devices/<int:pk>/weather-data/', DeviceDetailsViewSet.as_view({'get': 'weather_data'}), name='device-weather-data'),
]
