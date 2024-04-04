from main.models import Temperatures, Humidities, Pressures, Lights
from main.sensors.light_sensor import LightSensor
from main.sensors.temperature_sensor import TemperatureSensor
from datetime import date

import threading, time


class SensorsManager(object):
    light_sensor = LightSensor()
    temperature_sensor = TemperatureSensor()

    def __init__(self):
        threading.Timer(30, self.write_to_db).start()

    def write_to_db(self):
        Temperatures.objects.create(value=self.temperature_sensor.temperature(), datetime=date.today())
        Humidities.objects.create(value=self.temperature_sensor.humidity(), datetime=date.today())
        Pressures.objects.create(value=self.temperature_sensor.pressure(), datetime=date.today())
        Lights.objects.create(value=self.light_sensor.light(), datetime=date.today())
        threading.Timer(30, self.write_to_db).start()
        #print("Temperature: %7.2f C" % self.temperature_sensor.temperature())
        return

