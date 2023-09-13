from jobs.utils.temperature import Temperature

if __name__ == "__main__":
    temperature_reader = Temperature()

    print(f"Current temperature is: {temperature_reader.read_temp()}°C")
