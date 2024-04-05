from django.shortcuts import render

from main.models import Temperatures, Humidities, Pressures, Lights
from main.sensors.sensor_manager import SensorsManager

sensor_manager = SensorsManager()


# Главная страница
def index(request):
    values = {
        'light_sensor': sensor_manager.light_sensor
    }
    return render(request, 'main/index.html', values)


# Предварительный просмотр значения датчика освещенности
def light_sensor(request):
    values = {
        'light_sensor': sensor_manager.light_sensor
    }
    return render(request, 'main/preview_sensors/light_sensor.html', values)


# Предварительный просмотр значения датчика температуры
def temperature_sensor(request):
    values = {
        'temperature_sensor': sensor_manager.temperature_sensor
    }
    return render(request, 'main/preview_sensors/temperature_sensor.html', values)


# Статистика по температуре
def temperatures_chart(request):
    temperatures = Temperatures.objects.all()
    values = {
        'temperatures': temperatures
    }
    return render(request, 'main/dashboard/temperatures.html', values)


# Статистика по влажности
def humidities_chart(request):
    humidities = Humidities.objects.all()
    values = {
        'humidities': humidities
    }
    return render(request, 'main/dashboard/humidities.html', values)


# Статистика по давлению
def pressures_chart(request):
    pressures = Pressures.objects.all()
    values = {
        'pressures': pressures
    }
    return render(request, 'main/dashboard/pressures.html', values)


# Статистика по освещенности
def lights_chart(request):
    lights = Lights.objects.all()
    values = {
        'lights': lights
    }
    return render(request, 'main/dashboard/lights.html', values)
