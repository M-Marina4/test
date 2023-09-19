from django.db import models
# Create your models here.

class Devices(models.Model):
    device_name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Armenia')

    def __str__(self):
        return self.device_name


class WeatherData(models.Model):
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    time = models.DateTimeField()
    light = models.FloatField()
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    pm1 = models.FloatField()
    pm2_5 = models.FloatField()
    pm10 = models.FloatField()
    atmospheric_pm1 = models.FloatField()
    atmospheric_pm2_5 = models.FloatField()
    atmospheric_pm10 = models.FloatField()
    co2 = models.FloatField() 
    speed = models.FloatField()
    rain = models.FloatField()
    direction = models.TextField()

    def __str__(self):
        return str(self.time)
