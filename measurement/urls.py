from django.urls import path
from .views import SensorView, SensorEditView, SensorCreateView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('post/', SensorView.as_view()),
    path('patch/<pk>/', SensorEditView.as_view()),
    path('create/', SensorCreateView.as_view()),
    path('temp/', MeasurementView.as_view()),
]
