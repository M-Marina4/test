from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views import DeviceDetailsViewSet

router = DefaultRouter()
router.register(r'device/1', DeviceDetailsViewSet, basename='device1')
router.register(r'device/2', DeviceDetailsViewSet, basename='device2')
urlpatterns = [
    path('api/', include(router.urls)),
    # Endpoint to list devices
    path('api/device/<int:pk>/', DeviceDetailsViewSet.as_view({'get': 'retrieve_device'}), name='device-details'),
    # Endpoint to create a new device (POST request)
    # path('api/devices/', DeviceDetailsViewSet.as_view({'post': 'create'}), name='create-device'),

    # Endpoint to get details of a specific device by ID
    #path('api/devices/<int:pk>/', DeviceDetailsViewSet.as_view({'get': 'retrieve'}), name='device-detail'),

    # Endpoint to get weather data for a specific device
    #path('api/devices/<int:pk>/weather_data/', DeviceDetailsViewSet.as_view({'get': 'weather_data'}), name='device-weather-data'),
]
