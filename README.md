# WeeWX - GrovePi
Integrating GrovePi with Weewx platform

This is a driver for weewx that interfaces GrovePI and its weather station components.

Installation

0) install weewx (see the weewx user guide)

1) download the driver

wget -O weewx-grovepi.zip https://github.com/sookah/weewx-grovepi/archive/master.zip

2) install the driver

wee_extension --install weewx-grovepi.zip

3) configure the driver

wee_config --reconfigure

4) start weewx

sudo /etc/init.d/weewx start
