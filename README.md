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

`sudo pip install config`


## The driver

### Changing the driver

`http://weewx.com/docs/utilities.htm#wee_config_utility`


## Testing the driver

run the `test_driver.sh` with:

```bash
# make it executable
sudo chmod +x test_driver.sh

# run
./test_driver.sh
```


