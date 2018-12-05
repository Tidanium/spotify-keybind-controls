import sys, dbus
from subprocess import Popen


sys.stdout = None  # let's get this out of the way first
spotify_dbus_command_base=r'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.'

async def next():
    return Popen(spotify_dbus_command_base+r'Next').communicate()


async def previous():
    return Popen(spotify_dbus_command_base+r'Previous').communicate()


async def toggle_play():
    return Popen(spotify_dbus_command_base+r'PlayPause').communicate()


async def stop():
    return Popen(spotify_dbus_command_base+r'Stop').communicate()


interface = dbus.Interface(dbus.SessionBus().get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2'), 'org.freedesktop.DBus.Properties')
"""
interface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
[dbus.String('mpris:trackid'),
 dbus.String('mpris:length'),
 dbus.String('mpris:artUrl'), 
 dbus.String('xesam:album'), 
 dbus.String('xesam:albumArtist'), 
 dbus.String('xesam:artist'), 
 dbus.String('xesam:autoRating'), 
 dbus.String('xesam:discNumber'), 
 dbus.String('xesam:title'), 
 dbus.String('xesam:trackNumber'), 
 dbus.String('xesam:url')]
"""


def is_paused():
    return True if interface.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus').__str__() == "Paused" else False


def get_url():
    return interface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')[dbus.String('xesam:url')].__str__()
