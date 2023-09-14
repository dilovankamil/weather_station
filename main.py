from jobs.utils.ds18b20_reader import DS18B20_Reader
from jobs.utils.bme280_reader import BME280_Reader

if __name__ == "__main__":
    ds18b20_reader = DS18B20_Reader()
    bme280_reader = BME280_Reader()

    pressure, humidity = bme280_reader.get_readings()

    print(f"Current temperature is: {ds18b20_reader.read_temp()}°C")
    print(f"Current humidity is: {humidity}%")
    print(f"Current pressure is: {pressure}hPa")
