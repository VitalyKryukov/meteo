from main.models import Temperatures, Humidities, Pressures, Lights
from main.sensors.light_sensor import LightSensor
from main.sensors.temperature_sensor import TemperatureSensor
from datetime import datetime
import threading
import logging


class SensorsManager(object):
    light_sensor = LightSensor()
    temperature_sensor = TemperatureSensor()

    def __init__(self):
        threading.Timer(60, self.write_to_db).start()

    def write_to_db(self):
        logging.info("Запись в базу данных новых параметров")
        Temperatures.objects.create(value=self.temperature_sensor.temperature(), datetime=datetime.now())
        Humidities.objects.create(value=self.temperature_sensor.humidity(), datetime=datetime.now())
        Pressures.objects.create(value=self.temperature_sensor.pressure(), datetime=datetime.now())
        Lights.objects.create(value=self.light_sensor.light(), datetime=datetime.now())
        threading.Timer(60, self.write_to_db).start()
        return
