from django.db import models
# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} - {self.pk}"

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.pk}"

class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor,on_delete=models.CASCADE)
    data = models.TextField()
    def __str__(self):
        return f"{self.pk}"
