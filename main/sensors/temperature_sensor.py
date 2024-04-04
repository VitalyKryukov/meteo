import bme280.bme280 as bme280


class TemperatureSensor:
    def __init__(self):
        bme280.bme280_i2c.set_default_i2c_address(0x76)
        bme280.bme280_i2c.set_default_bus(3)
        bme280.setup()

    def temperature(self):
        data_all = bme280.read_all()
        #print("%7.2f C" % data_all.temperature)
        return round(data_all.temperature, 2)

    def humidity(self):
        data_all = bme280.read_all()
        #print("%7.2f %%" % data_all.humidity)
        return round(data_all.humidity, 2)

    def pressure(self):
        data_all = bme280.read_all()
        #print("%7.2f hPa" % data_all.pressure)
        return round(data_all.pressure, 2)
