# !/usr/bin/python
#
# Copyright 2018 Saujan Ghimire
# Read data from GroveWeatherPi

import time
import math
import logging
import json

from tentacle_pi.AM2315 import AM2315

from SDL_Pi_WeatherRack import SDL_Pi_WeatherRack

DEBUG_SERIAL = 0  # type: bool
LOG_FILE = '/var/log/wxgrovepi.log'
LIVE_DATA_FILE = '/var/tmp/wxgrovepidata'

logger = logging.getLogger(__name__)

LOG_FORMAT = '''[%(asctime)s] -  { %(filename)s:%(lineno)d } | %(levelname)s - %(message)s'''
formatter = logging.Formatter(LOG_FORMAT)
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)


class GrovePiWeatherStation(object):
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

    def save_to_file(self, filename):
        with open(filename, mode='w') as f:
            f.write('outTemp = %s\n' % (self.get_temp()))
            f.write('outHumidity = %s\n' % (self.get_humidity()))

    def get_data_as_json(self):
        return json.dumps({
            "outTemp": self.get_temp(),
            "outHumidity": self.get_humidity()
        })


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
class GrovePiWeatherRack(object):
    def __init__(self):
        # GPIO Numbering Mode GPIO.BCM

        ANENOMETER_PIN = 26
        RAIN_PIN = 21

        # constants

        SDL_MODE_INTERNAL_AD = 0
        SDL_MODE_I2C_ADS1015 = 1

        # sample mode means return immediately.  THe wind speed is averaged at sampleTime or when you ask, whichever is longer
        SDL_MODE_SAMPLE = 0
        # Delay mode means to wait for sampleTime and the average after that time.
        SDL_MODE_DELAY = 1

        self.weatherStation = SDL_Pi_WeatherRack.SDL_Pi_WeatherRack(
            ANENOMETER_PIN, RAIN_PIN, 0, 0, SDL_MODE_I2C_ADS1015)

        self.weatherStation.setWindMode(SDL_MODE_SAMPLE, 5.0)

    # custom function to get the values from the sensor
    def get_all(self):
        maxEverWind = 0.0
        maxEverGust = 0.0
        totalRain = 0

        currentWindSpeed = self.weatherStation.current_wind_speed() / 1.609
        currentWindGust = self.weatherStation.get_wind_gust() / 1.609
        totalRain = totalRain + \
                    (self.weatherStation.get_current_rain_total() / 25.4)

        if currentWindSpeed > maxEverWind:
            maxEverWind = currentWindSpeed

        if currentWindGust > maxEverGust:
            maxEverGust = currentWindGust


        # TODO fix this funciton here
        # return self.reiknaVindatt(self.weatherStation.current_wind_direction()) + (" %0.1f m/s") % (currentWindSpeed)

    # svaka flotta vindutreikningafallid okkar!
    def reiknaVindatt(self, vindur):
        # do lot of stuff (TM)

        val = int(math.floor(vindur / 22.5))
        arr = ["N", "NNA", "NA", "ANA", "A", "ASA", "SA", "SSA",
               "S", "SSV", "SV", "VSV", "V", "VNV", "NV", "NNV"]

        return arr[(val % 16)]


if __name__ == '__main__':
    logging.info("Starting GrovePI Weather station app")

    try:
        # Instantiate GrovePi
        grove_pi = GrovePiWeatherStation()

        logging.info('getting live data')

        while True:
            # update all sensors data
            grove_pi.update_data()
            print (grove_pi.get_data_as_json())
            grove_pi.save_to_file(LIVE_DATA_FILE)
            grove_pi.weather.get_all()

            time.sleep(2)

    except Exception as e:
        logging.exception("Program ran into error: %s", e)
