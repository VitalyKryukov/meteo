import bme280.bme280 as bme280
import logging


# Класс для работы с датчиком температуры, влажности и давления
class TemperatureSensor:
    def __init__(self):
        try:
            bme280.bme280_i2c.set_default_i2c_address(0x76)  # Установка адреса датчика
            bme280.bme280_i2c.set_default_bus(3)  # Установка номера шины
            bme280.setup()  # Инициализация датчика
        except Exception as e:
            logging.exception(f'Произошла ошибка при инициализации датчика температуры {e}')

    # Функция для получения значения температуры
    def temperature(self):
        try:
            data_all = bme280.read_all()
        except Exception as e:
            logging.exception(f'Произошла ошибка при получении данных {e}')
            return -1
        return round(data_all.temperature, 2)

    # Функция для получения значения влажности
    def humidity(self):
        try:
            data_all = bme280.read_all()
        except Exception as e:
            logging.exception(f'Произошла ошибка при получении данных {e}')
            return -1
        return round(data_all.humidity, 2)

    # Функция для получения значения давления
    def pressure(self):
        try:
            data_all = bme280.read_all()
        except Exception as e:
            logging.exception(f'Произошла ошибка при получении данных {e}')
            return -1
        return round(data_all.pressure, 2)
