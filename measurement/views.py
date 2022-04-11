# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, AllSensorSerializer

# 1 option
# @api_view(['GET', 'POST'])
# def sensor(request):
#     if request.method == 'GET':
#         sensors = Sensor.objects.all()
#         ser = SensorSerializer(sensors, many=True)
#         return Response(ser.data)
#     if request.method == 'POST':
#         return Response({'status': 'OK'})


# 2 option
# class SensorView(APIview):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         ser = SensorSerializer(sensors, many=True)
#         return Response(ser.data)
#     def post(self, request):
#         return Response({'status': 'OK'})

# 3 option
class SensorView(ListCreateAPIView):   #POST
    queryset = Sensor.objects.all()
    serializer_class = AllSensorSerializer


class SensorEditView(RetrieveUpdateAPIView):  #patch
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorCreateView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer