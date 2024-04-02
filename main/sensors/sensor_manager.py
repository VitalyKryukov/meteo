from main.models import Temperatures
from main.sensors.light_sensor import LightSensor
from main.sensors.temperature_sensor import TemperatureSensor
from datetime import date

import threading, time


class SensorsManager(object):
    light_sensor = LightSensor()
    temperature_sensor = TemperatureSensor()

    def __init__(self):
        self.write_to_db()

    def write_to_db(self):
        Temperatures.objects.create(value=self.temperature_sensor.temperature(), datetime=date.today())
        threading.Timer(1, self.write_to_db).start()
        print("Temperature: %7.2f C" % self.temperature_sensor.temperature())
        return

