# installer for wxgrovepi driver

from setup import ExtensionInstaller


def loader():
    return WXGrovePiInstaller()


class WXGrovePiInstaller(ExtensionInstaller):
    def __init__(self):
        super(WXGrovePiInstaller, self).__init__(
            version="0.1",
            name='wxgrovepi',
            description='weewx driver for GrovePi.',
            author="Saujan Ghimire",
            author_email="",
            config={
                'Station': {
                    'station_type': 'GrovePi'},
                'GrovePi': {
                    'poll_interval': '10',
                    'path': '/var/tmp/datafile',
                    'driver': 'user.wxgrovepi'}},
            files=[('bin/user', ['bin/user/wxgrovepi.py'])]
        )
