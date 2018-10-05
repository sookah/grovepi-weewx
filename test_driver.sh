#!/usr/bin/env bash

echo "Testing the driver"

sudo PYTHONPATH=/usr/share/weewx:/home/pi/SDL_Pi_GroveWeatherPi/SDL_Pi_WeatherRack/\
:/home/pi/SDL_Pi_GroveWeatherPi/SDL_Adafruit_ADS1x15/ python bin/user/wxgrovepi.py  --debug

echo "Done"