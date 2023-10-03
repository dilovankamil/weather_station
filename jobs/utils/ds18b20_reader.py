import os
import glob
import time


class DS18B20_Reader:
    def __init__(self) -> None:
        os.system("modprobe w1-gpio")
        os.system("modprobe w1-therm")

        self.base_dir = "/sys/bus/w1/devices/"
        self.device_folder = glob.glob(self.base_dir + "28*")[0]
        self.device_file = self.device_folder + "/w1_slave"
        print("DS18B20_Reader initialized")

    # Reading w1 slave and returns its results
    def _read_temp_raw(self) -> str:
        f = open(self.device_file, "r")
        lines = f.readlines()
        f.close()
        return lines

    # Returns the temperature in Celsius
    def read_temp(self) -> float:
        print("Reading temperature...")
        lines = self._read_temp_raw()
        equals_pos = lines[1].find("t=")
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2 :]
            return float(temp_string) / 1000.0
