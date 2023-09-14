from jobs.utils.temperature import Temperature
from jobs.utils.humidity import Humidity

if __name__ == "__main__":
    temperature_reader = Temperature()
    humidity_reader = Humidity()

    pressure, humidity = humidity_reader.get_readings()

    print(f"Current temperature is: {temperature_reader.read_temp()}°C")
    print(f"Current humidity is: {humidity}%")
    print(f"Current pressure is: {pressure}hPa")
