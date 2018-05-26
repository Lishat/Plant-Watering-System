from __future__ import unicode_literals
from django.db import models
class Sensors(models.Model):
    serialId = models.CharField(default="Not Received", max_length = 100)
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    pressure = models.FloatField(default=0)
    altitude = models.FloatField(default=0)
    seaPressure = models.FloatField(default=0)
    soilMoisture = models.FloatField(default=0)
    soilMoisture2 = models.FloatField(default=0)
    waterLevel = models.FloatField(default=0)
    rainDrop = models.FloatField(default=0)
    ultrasonic = models.FloatField(default=0)
    time = models.CharField(default="Not Received", max_length = 100)
    def __str__(self):
        return str(self.serialId) + ' ' + str(self.temperature) + ' ' + str(self.humidity) + ' ' + str(self.pressure) + ' ' + str(self.altitude) + ' ' + str(self.seaPressure) + ' ' + str(self.soilMoisture) + ' ' + str(self.soilMoisture2) + ' ' + str(self.waterLevel) + ' ' + str(self.rainDrop) +' '+str(self.ultrasonic)+ ' ' + str(self.time)
class decide(models.Model):
    value = models.IntegerField(default=0)
class moto1(models.Model):
    value = models.IntegerField(default=0)
class moto2(models.Model):
    value = models.IntegerField(default=0)