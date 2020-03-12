from threading import Thread
import time
from shutil import copyfile


class HDFSSender(Thread):
    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, file_path_in, file_path_out, interval):
        Thread.__init__(self)
        self._in = file_path_in
        self._out = file_path_out
        self._interval = interval

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        timestamp = 0
        while 1:
            if time.clock() - timestamp > self._interval:
                timestamp += time.clock()
                copyfile(self._in, self._out)
