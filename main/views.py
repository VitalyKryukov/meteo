from django.shortcuts import render
from main.sensors.sensor_manager import SensorsManager

sensor_manager = SensorsManager()


# Create your views here.
def index(request):
    values = {
        'light_sensor': sensor_manager.light_sensor
    }
    return render(request, 'main/index.html', values)


def light_sensor(request):
    values = {
        'light_sensor': sensor_manager.light_sensor
    }
    return render(request, 'main/preview_sensors/light_sensor.html', values)


def dashboard(request):
    return render(request, 'main/dashboard.html')
