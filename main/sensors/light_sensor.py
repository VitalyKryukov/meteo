from apds9930 import APDS9930
from apds9930.values import ALL, OFF
from time import sleep


# Класс для работы с датчиком освещенности
class LightSensor:
    busno = int(3)  # Установка номера шины для датчика
    a = APDS9930(busno)  # Инициализация датчика

    def __init__(self):
        self.a.enable_ambient_light_sensor()  # Включение датчика освещенности
        self.a.enable_proximity_sensor()  # Включение датчика приближения
        self.a.set_mode(0, 1)
        self.a.set_mode(1, 1)
        self.a.set_mode(2, 1)
        pass

    # Функция по получению значения освещенности
    def light(self):
        print(round(self.a.ambient_light, 1))
        return round(self.a.ambient_light, 1)

    # Функция по получению значения приближения
    def proximity(self):
        return self.a.proximity
