# installer for wxgrovepi driver

from setup import ExtensionInstaller


def loader():
    return WXGrovePiInstaller()


class WXGrovePiInstaller(ExtensionInstaller):
    def __init__(self):
        super(WXGrovePiInstaller, self).__init__(
            version="0.3",
            name='wxgrovepifp',
            description='weewx driver for GrovePi.',
            author="Saujan Ghimire",
            author_email="",
            config={
                'Station': {'station_type': 'wxgrovepifp'},
                'wxgrovepifp': {
                    'loop_interval': '10',
                    'path': '/var/tmp/wxgrovepidata',
                    'driver': 'user.wxgrovepifp'}},
            files=[('bin/user', ['bin/user/wxgrovepifp.py'])]
        )
