import pytest
from television import *

class Test():
    def setup_method(self):
        self.t1 = Television()

    def teardown_method(self):
        del self.t1

    def test_init(self):
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        #tv is on
        self.t1.power()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"

        #tv is off
        self.t1.power()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        #tv is on, vol increased once, then tv muted
        self.t1.power()
        self.t1.volume_up()
        self.t1.mute()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"

        #tv is on and unmuted
        self.t1.mute()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 1"

        #tv is off and muted
        self.t1.power()
        self.t1.mute()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 1"

        #tv is off and unmuted
        self.t1.mute()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 1"

    def test_channel_up(self):
        #tv is off and channel increased
        self.t1.channel_up()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 0"

        #tv is on and channel increased
        self.t1.power()
        self.t1.channel_up()
        assert self.t1.__str__() == "Power = True, Channel = 1, Volume = 0"

        #tv is on and channel increases past max value
        self.t1.channel_up()
        self.t1.channel_up()
        assert self.t1.__str__() == "Power = True, Channel = 3, Volume = 0"
        self.t1.channel_up()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        #tv is off and channel decreased
        self.t1.channel_down()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 0"

        #tv is on and channel decreased past minimum value
        self.t1.power()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.t1.channel_down()
        assert self.t1.__str__() == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        #tv is off and vol increased
        self.t1.volume_up()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 0"

        #tv is on and vol increased
        self.t1.power()
        self.t1.volume_up()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 1"

        #tv is on, muted, and vol increased
        self.t1.mute()
        self.t1.volume_up()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 2"

        #tv is on and vol increased past max value
        self.t1.volume_up()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        #tv is off and vol decreased
        self.t1.volume_down()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 0"

        #tv is on and volume decreased
        self.t1.power()
        self.t1.volume_up()
        self.t1.volume_up()
        self.t1.volume_down()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 1"

        #tv is on, muted, and vol decreased
        self.t1.mute()
        self.t1.volume_down()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"

        #tv is on and vol decreased past min value
        self.t1.volume_down()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"