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
        self.name = DRIVER_NAME
        self.loop_interval = float(stn_dict.get('loop_interval', 5))

    @property
    def hardware_name(self):
        return self.name

    def genLoopPackets(self):
        pass


class GrovePiStation:
    """
    GrovePi Class to grab data from various sensors
    """

    def __init__(self):
        pass

    def get_temp(self):
        pass

    def get_humidity(self):
        pass

    def get_wind(self):
        # Via Anemometer
        pass

    def get_rain(self):
        # via Anemometer
        pass


# TODO: These classes maynot be required later abstract everything to a grovePIStation
# class SensorAM2315:
#     """
#     Sensor AM2315 with temperature and humidity measurement
#     """
#
#     def __init__(self):
#         pass
#
#     def get_temp(self):
#         pass
#
#     def get_humidity(self):
#         pass
#

# define a main entry point for basic testing of the station without weewx
# engine and service overhead.  invoke this as follows from the weewx root dir:
#
# PYTHONPATH=bin python bin/weewx/drivers/grovepi.py


if __name__ == '__main__':
    driver = WXGrovePi()
