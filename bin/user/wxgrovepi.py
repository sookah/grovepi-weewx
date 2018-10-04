#!/usr/bin/python
#
# Copyright 2018 Saujan Ghimire
#
# weewx driver that reads data from GrovePi Weather Station
#

from __future__ import with_statement
from __future__ import print_function

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
        pass

    def get_temp(self):
        pass

    def get_humidity(self):
        pass

    def get_anemometer_data(self):
        pass

    def get_wind_data(self):
        pass

    def get_rain_data(self):
        pass


import time
from tentacle_pi.AM2315 import AM2315


# TODO: These classes maynot be required later abstract everything to a grovePIStation
class SensorAM2315(object):
    """
    Sensor AM2315 with temperature and humidity measurement
    """

    def __init__(self, i2c_bus="/dev/i2c-1"):
        i2c_adress = 0x5c
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

# define a main entry point for basic testing of the station without weewx
# engine and service overhead.  invoke this as follows from the weewx root dir:
# PYTHONPATH=bin python bin/weewx/drivers/grovepi.py


if __name__ == '__main__':
    driver = WXGrovePi()
