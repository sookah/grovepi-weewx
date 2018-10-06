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

## WeeWx

Common files location

Configuration : `/etc/weewx/weewx.conf`

Status : `sudo service weewx status`

Force generate a report : `sudo  wee_reports weewx.conf`


3.  Start weewx

```
sudo /etc/init.d/weewx start
```


### The manual approach: modify weewx.conf

Since we have our own driver we will have to use this approach. This approach will work on any weewx installation for both standard and custom drivers.

1. Stop weewx

```
sudo /etc/init.d/weewx stop
```

2.  Modify weewx.conf

    For example, to specify the Vantage driver for Davis Vantage Pro2 hardware:

```
    [Station]
        ...
        station_type = Vantage

    [Vantage]
        type = serial
        port = /dev/ttyUSB0
        driver = weewx.drivers.vantage
```

3.  Start weewx

```
sudo /etc/init.d/weewx start
```



### The weewx approach: run wee_config

This approach will work on any weewx installation for standard drivers and/or drivers in the user directory.

1.  Stop weewx

```
sudo /etc/init.d/weewx stop
```

2.  Run wee_config with the reconfigure option:

```
sudo wee_config --reconfigure
```

3.  Start weewx

```
sudo /etc/init.d/weewx start
```

The wee_config command should prompt for the station parameters, including the station type and any options required by the station.

