from main.sensors.light_sensor import LightSensor
from main.sensors.temperature_sensor import TemperatureSensor


class SensorsManager(object):
    light_sensor = LightSensor()
    temperature_sensor = TemperatureSensor()

    def __init__(self):
        pass
