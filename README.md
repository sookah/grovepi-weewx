# WeeWX - GrovePi

> Integrating GrovePi with Weewx platform

This is a driver for weewx that interfaces GrovePI and its weather station components.

## Installation

1. install weewx (see the weewx user guide)

2. download the driver

    `wget -O weewx-grovepi.zip https://github.com/sookah/weewx-grovepi/archive/master.zip`
3. install the driver
    
    `wee_extension --install weewx-grovepi.zip`

4. configure the driver

    `wee_config --reconfigure`

5. start weewx

    `sudo /etc/init.d/weewx start`

### Additional installation

Following additional packages are needed for the package (also in setup.py)

`pip install config`


## The driver

### Changing the driver

`http://weewx.com/docs/utilities.htm#wee_config_utility`


## Testing the driver

load all the modules in the PYTHONPATH and run
```bash
PYTHONPATH=/usr/share/weewx:/home/pi/SDL_Pi_GroveWeatherPi/SDL_Pi_WeatherRack/:/home/pi/SDL_Pi_GroveWeatherPi/SDL_Adafruit_ADS1x15/ python wxgrovepi.py  --debug
```