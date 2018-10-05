#!/usr/bin/python
#
# Copyright 2018 Saujan Ghimire
#
# weewx driver that reads data from GrovePi Weather Station
#

from __future__ import print_function
from __future__ import with_statement

import weewx.drivers

DRIVER_NAME = 'grovepi'  # type: str
DRIVER_VERSION = '0.1'  # type: str

DEBUG_SERIAL = 0  # type: bool


# Define the loader
def loader(config_dict, engine):
    return WXGrovePi(**config_dict[DRIVER_NAME])


def confeditor_loader():
    return WXGrovePi()


class WXGrovePi(weewx.drivers.AbstractDevice):
    """
        weewx driver that communicates with an GrovePi Weather Station
    """
    global DRIVER_NAME

    def __init__(self, **stn_dict):
        """Initialize the simulator
        NAMED ARGUMENTS:
        loop_interval: The time (in seconds) between emitting LOOP packets.
        [Optional. Default is 2.5]`
        :param stn_dict:
        """
        self.name = DRIVER_NAME
        self.loop_interval = float(stn_dict.get('loop_interval', 5))

    @property
    def hardware_name(self):
        return self.name

    def genLoopPackets(self):
        pass


class GrovePiWeatherStation:
    """
    GrovePi Class to grab data from various sensors
    """

    def __init__(self):
        self.temp_sensor = SensorAM2315()
        self.weather = GrovePiWeatherRack()

    def update_data(self):
        # get AM2315 data
        self.temp_sensor.get_data()

    def get_temp(self):
        return round(self.temp_sensor.get_temp(), 1)

    def get_humidity(self):
        return round(self.temp_sensor.get_humidity(), 1)

    def get_anemometer_data(self):
        pass

    def get_wind_data(self):
        pass

    def get_rain_data(self):
        pass


from tentacle_pi.AM2315 import AM2315


class SensorAM2315(object):
    """
    Sensor AM2315 with temperature and humidity measurement
    """

    def __init__(self, i2c_adress=0x5c, i2c_bus="/dev/i2c-1"):
        self.am = AM2315(i2c_adress, i2c_bus)
        self.temperature = 0
        self.humidity = 0
        self.crc_check = 0

    def get_data(self):
        self.temperature, self.humidity, self.crc_check = self.am.sense()

    def get_temp(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity


# imports

import time
import sys
import math

sys.path.append('../Adafruit_ADS1x15')
sys.path.append('../')

import config

import SDL_Pi_WeatherRack as SDL_Pi_WeatherRack


class GrovePiWeatherRack(object):
    def __init__(self):
        # GPIO Numbering Mode GPIO.BCM
        #
        anenometerPin = 26
        rainPin = 21

        # constants

        SDL_MODE_INTERNAL_AD = 0
        SDL_MODE_I2C_ADS1015 = 1

        # sample mode means return immediately.  THe wind speed is averaged at sampleTime or when you ask, whichever is longer
        SDL_MODE_SAMPLE = 0
        # Delay mode means to wait for sampleTime and the average after that time.
        SDL_MODE_DELAY = 1

        self.weatherStation = SDL_Pi_WeatherRack.SDL_Pi_WeatherRack(
            anenometerPin, rainPin, 0, 0, SDL_MODE_I2C_ADS1015)

        self.weatherStation.setWindMode(SDL_MODE_SAMPLE, 5.0)

    # custom function to get the values from the sensor
    def get__all(self):
        maxEverWind = 0.0
        maxEverGust = 0.0
        totalRain = 0
        for count in range(10):
            currentWindSpeed = self.weatherStation.current_wind_speed() / 1.609
            currentWindGust = self.weatherStation.get_wind_gust() / 1.609
            totalRain = totalRain + \
                        (self.weatherStation.get_current_rain_total() / 25.4)

            if currentWindSpeed > maxEverWind:
                maxEverWind = currentWindSpeed

            if currentWindGust > maxEverGust:
                maxEverGust = currentWindGust

            time.sleep(1.0)

        # TODO fix this funciton here
        # return self.reiknaVindatt(self.weatherStation.current_wind_direction()) + (" %0.1f m/s") % (currentWindSpeed)

    # svaka flotta vindutreikningafallid okkar!
    def reiknaVindatt(self, dummy, vindur):
        # do lot of stuff (TM)

        val = int(math.floor(vindur / 22.5))
        arr = ["N", "NNA", "NA", "ANA", "A", "ASA", "SA", "SSA",
               "S", "SSV", "SV", "VSV", "V", "VNV", "NV", "NNV"]

        return arr[(val % 16)]


# define a main entry point for basic testing of the station without weewx
# engine and service overhead.  invoke this as follows from the weewx root dir:
# PYTHONPATH=bin python bin/weewx/drivers/grovepi.py

if __name__ == '__main__':
    print("Running wxgrovepi")
    driver = WXGrovePi()

    test_grovepi = GrovePiWeatherStation()
    for i in range(0, 3):
        test_grovepi.update_data()
        print(test_grovepi.get_temp())
        print(test_grovepi.get_humidity())
        time.sleep(0.2)
