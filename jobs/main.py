from datetime import datetime
import time
import statistics
import math

from gpiozero import Button
from utils.ds18b20_reader import DS18B20_Reader
from utils.bme280_reader import BME280_Reader
from utils.wind_direction import get_value as get_wind_direction
from utils.wind_direction import get_average as get_wind_direction_average


def spin():
    global wind_count
    wind_count = wind_count + 1


def calculate_wind_speed(time_sec):
    global wind_count
    circumference_in_cm = (2 * math.pi) * 9  # The radius of the arm is 9 cm
    rotations = wind_count / 2.0  # Because the apparatus "clicks" every half rotation

    dist_in_cm = circumference_in_cm * rotations
    cm_per_second = dist_in_cm / time_sec

    return (
        cm_per_second / 100
    ) * 1.18  # Because of loss in the mechanics of the measurment device


def reset_wind():
    global wind_count
    wind_count = 0


wind_speed_sensor = Button(5)
wind_speed_sensor.when_activated = spin
wind_interval = 5

if __name__ == "__main__":
    ds18b20_reader = DS18B20_Reader()
    bme280_reader = BME280_Reader()

    store_speeds = []
    store_directions = []

    while True:
        print(f"Starting job at {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}")
        start_time = time.time()
        while time.time() - start_time <= 300:  # 5 * 60 seconds = 300
            wind_start_time = time.time()
            reset_wind()
            while time.time() - wind_start_time <= wind_interval:
                store_directions.append(get_wind_direction(wind_interval))
            final_speed = calculate_wind_speed(wind_interval)
            store_speeds.append(final_speed)
        print("Getting wind gust speed...")
        wind_gust = max(store_speeds)
        print("Getting average wind speed...")
        wind_speed = statistics.mean(store_speeds)
        print("Getting average wind direction...")
        wind_direction = get_wind_direction_average(store_directions)
        store_speeds = []
        store_directions = []

        pressure, humidity = bme280_reader.get_readings()
        temperature = ds18b20_reader.read_temp()

        with open("dump.txt", "w") as f:
            f.write(
                f"Current temperature is: {temperature}°C\nCurrent humidity is: {humidity}%\nCurrent pressure is: {pressure}hPa\nWind speed is: {wind_speed}m/s\nWind gust is: {wind_gust}m/s\nWind direction is: {wind_direction}°\nAt time: {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}"
            )

        print(f"Finishing job at {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}")
