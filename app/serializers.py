from rest_framework import serializers
from app import models

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SensorData
        fields = [ 'url']+ [ f.name for f in model._meta.fields ]
        depth = 2

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sensor
        fields = [ 'url']+ [ f.name for f in model._meta.fields ]
        read_only_fields = ('id',)
        depth=1
    def to_representation(self, instance):
        response = super().to_representation(instance)
        d= list(instance.sensordata_set.all().values())
        _s = SensorDataSerializer(data=d,many=True)
        if _s.is_valid():
            _data = [ x['data'] for x in d ]
            response['DataSet'] = _data
        return response

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = [ 'url']+ [ f.name for f in model._meta.fields ] 
        read_only_fields = ('id',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        d= list(instance.sensor_set.all().values())
        _s = SensorSerializer(data=d,many=True)
        if _s.is_valid():
            _data = [ {"id":x["id"],"name":x['name']} for x in d ]
            response['sensor'] = _data
        return response

    def create(self, validated_data):
        print("create metho is called.")
        _obj= super().create(validated_data)
        _default_sensor = ['Temperature Sensor','Pressure Sensor']
        for _s in _default_sensor:
            _sensor = models.Sensor()
            _sensor.name = _s
            _sensor.save()
        return _obj
