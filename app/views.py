from django.shortcuts import render

# Create your views here.
from app import models
from rest_framework import serializers, viewsets
from rest_framework import permissions
from app.serializers import *  


class Device_ViewSet(viewsets.ModelViewSet):
    queryset = models.Device.objects.all().order_by('-pk')
    serializer_class = DeviceSerializer
    http_method_names = ['get', 'post', 'head', 'put']
    name = 'device-viewset'

class Sensor_ViewSet(viewsets.ModelViewSet):
    queryset = models.Sensor.objects.all().order_by('-pk')
    serializer_class = SensorSerializer
    http_method_names = ['get', 'post', 'head', 'put']

class SensorData_ViewSet(viewsets.ModelViewSet):
    queryset = models.SensorData.objects.all().order_by('-pk')
    serializer_class = SensorDataSerializer
    http_method_names = ['get', 'post', 'head', 'put']