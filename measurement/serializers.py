from rest_framework import serializers
from .models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы


# class SensorSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()
#
#
#
# class MeasurementSerializer(serializers.Serializer):
#     temperature = serializers.IntegerField()
#     date = serializers.DateField()

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'date']


class SensorSerializer(serializers.ModelSerializer):
    temperatures = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'temperatures']

class AllSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


