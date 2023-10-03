try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280


class BME280_Reader:
    def __init__(self) -> None:
        bus = SMBus(1)
        self.bme280 = BME280(i2c_dev=bus)
        self.bme280.setup(mode="forced")
        print("BME280_Reader initialized")

    def get_readings(self) -> tuple:
        print("Getting pressure and humidity...")
        pressure = self.bme280.get_pressure()
        humidity = self.bme280.get_humidity()

        return (pressure, humidity)
