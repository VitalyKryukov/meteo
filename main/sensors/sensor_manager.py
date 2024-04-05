from main.models import Temperatures, Humidities, Pressures, Lights
from main.sensors.light_sensor import LightSensor
from main.sensors.temperature_sensor import TemperatureSensor
from datetime import datetime
import threading
import logging


# Класс для работы сбора и созранения данных с датчиков
class SensorsManager(object):
    light_sensor = LightSensor()  # Инициализация объекта датчика освещенности
    temperature_sensor = TemperatureSensor()  # Инициализация объекта датчика температуры, влажности и давления

    def __init__(self):
        threading.Timer(60, self.write_to_db).start()  # Инициализация записи в базу данных через 60 секунд

    # Функция записи в базу данных
    def write_to_db(self):
        logging.info("Запись в базу данных новых параметров")
        Temperatures.objects.create(value=self.temperature_sensor.temperature(), datetime=datetime.now().astimezone())
        Humidities.objects.create(value=self.temperature_sensor.humidity(), datetime=datetime.now().astimezone())
        Pressures.objects.create(value=self.temperature_sensor.pressure(), datetime=datetime.now().astimezone())
        Lights.objects.create(value=self.light_sensor.light(), datetime=datetime.now().astimezone())
        threading.Timer(60, self.write_to_db).start()  # Запуск следующей записи в базу данных через 60 секунд
        return
