#!/usr/bin/env python

from __future__ import with_statement
from __future__ import print_function

import weewx.drivers

DRIVER_NAME = 'grovepi'
DRIVER_VERSION = '0.1'

DEBUG_SERIAL = 0


class GrovePi(weewx.drivers.AbstractDevice):
    """
        weewx driver that communicates with an GrovePi Weather Station

    """

    def __init__(self):
        self.name = "GrovePi"

    @property
    def hardware_name(self):
        return self.name

    def genLoopPackets(self):
        pass


class GrovePiStation:
    """
    GrovePi Class to grab data
    """
    def __init__(self):
        pass

# define a main entry point for basic testing of the station without weewx
# engine and service overhead.  invoke this as follows from the weewx root dir:
#
# PYTHONPATH=bin python bin/weewx/drivers/grovepi.py

if __name__ == '__main__':
    import optparse
