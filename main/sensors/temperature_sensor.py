import bme280.bme280 as bme280
import logging


class TemperatureSensor:
    def __init__(self):
        try:
            bme280.bme280_i2c.set_default_i2c_address(0x76)
            bme280.bme280_i2c.set_default_bus(3)
            bme280.setup()
        except Exception as e:
            logging.exception(f'Произошла ошибка при инициализации датчика температуры {e}')

    def temperature(self):
        try:
            data_all = bme280.read_all()
        except Exception as e:
            logging.exception(f'Произошла ошибка при получении данных {e}')
            return -1
        return round(data_all.temperature, 2)

    def humidity(self):
        try:
            data_all = bme280.read_all()
        except Exception as e:
            logging.exception(f'Произошла ошибка при получении данных {e}')
            return -1
        return round(data_all.humidity, 2)

    def pressure(self):
        try:
            data_all = bme280.read_all()
        except Exception as e:
            logging.exception(f'Произошла ошибка при получении данных {e}')
            return -1
        return round(data_all.pressure, 2)
