from apds9930 import APDS9930
from apds9930.values import ALL, OFF
from time import sleep


class LightSensor:
    busno = int(3)
    a = APDS9930(busno)

    def __init__(self):
        self.a.enable_ambient_light_sensor()
        self.a.enable_proximity_sensor()
        self.a.set_mode(0, 1)
        self.a.set_mode(1, 1)
        self.a.set_mode(2, 1)
        pass

    def light(self):
        print(round(self.a.ambient_light, 1))
        return round(self.a.ambient_light, 1)

    def proximity(self):
        return self.a.proximity
