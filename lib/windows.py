import importlib

try:
    spotify = importlib.import_module("spotipy", "spotipy")
except ImportError:
    from subprocess import Popen
    Popen(['pip', 'install', 'https://github.com/plamere/spotipy/archive/master.zip']).communicate()
    spotify = importlib.import_module("spotipy", "spotipy")
