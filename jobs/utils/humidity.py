try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280

class Humidity():
    def __init__(self) -> None:
        bus = SMBus(1)
        self.bme280 = BME280(i2c_dev=bus)

    def get_readings(self) -> tuple:
        pressure = self.bme280.get_pressure()
        humidity = self.bme280.get_humidity()
        return (pressure, humidity)
