from django.shortcuts import render

from main.models import Temperatures, Humidities, Pressures, Lights
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


def temperature_sensor(request):
    values = {
        'temperature_sensor': sensor_manager.temperature_sensor
    }
    return render(request, 'main/preview_sensors/temperature_sensor.html', values)


def dashboard(request):
    temperatures = Temperatures.objects.all()
    values = {
        'temperatures': temperatures
    }
    return render(request, 'main/dashboard/dashboard_layout.html', values)


def temperatures_chart(request):
    temperatures = Temperatures.objects.all()
    values = {
        'temperatures': temperatures
    }
    return render(request, 'main/dashboard/temperatures.html', values)


def humidities_chart(request):
    humidities = Humidities.objects.all()
    values = {
        'humidities': humidities
    }
    return render(request, 'main/dashboard/humidities.html', values)


def pressures_chart(request):
    pressures = Pressures.objects.all()
    values = {
        'pressures': pressures
    }
    return render(request, 'main/dashboard/pressures.html', values)


def lights_chart(request):
    lights = Lights.objects.all()
    values = {
        'lights': lights
    }
    return render(request, 'main/dashboard/lights.html', values)
