from rest_framework import serializers
from backend.models import Devices, WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'

class DeviceDetailsSerializer(serializers.ModelSerializer):
    weather_data = WeatherDataSerializer(many=True, read_only=True)

    class Meta:
        model = Devices
        fields = '__all__'

