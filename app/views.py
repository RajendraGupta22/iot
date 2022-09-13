from django.shortcuts import render

# Create your views here.
from app import models
from rest_framework import serializers, viewsets
from rest_framework import permissions
from app.serializers import *  
from rest_framework.permissions import SAFE_METHODS


class Device_ViewSet(viewsets.ModelViewSet):
    queryset = models.Device.objects.all().order_by('-pk')
    serializer_class = DeviceSerializer
    http_method_names = ['get', 'post', 'head', 'put']
    name = 'device-viewset'

class Sensor_ViewSet(viewsets.ModelViewSet):
    queryset = models.Sensor.objects.all().order_by('-pk')
    http_method_names = ['get', 'post', 'head', 'put']
    def get_serializer_class(self):
        if not self.request.method in SAFE_METHODS:
            return SensorReadSerializer
        return SensorSerializer

class SensorData_ViewSet(viewsets.ModelViewSet):
    queryset = models.SensorData.objects.all().order_by('-pk')
    # serializer_class = SensorDataSerializer
    http_method_names = ['get', 'post', 'head', 'put']
    def get_serializer_class(self):
        if not self.request.method in SAFE_METHODS:
            return ReadSensorDataSerializer
        return SensorDataSerializer