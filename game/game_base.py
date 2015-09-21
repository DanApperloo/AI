__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'


#########################################################################
# Imports
#########################################################################


#########################################################################
# Functions
#########################################################################
class BaseGame(object):

    def __init__(self):
        self._enable_replay = False
        self._enable_local_display = False
        self._local_display = None
        self._interface = None
        self._player_ids = 1

    def enable_replay(self):
        self._enable_replay = True

    def enable_local_display(self):
        self._enable_local_display = False

    def disable_replay(self):
        self._enable_replay = False

    def disable_local_display(self):
        self._enable_local_display = False

    def set_local_display(self, local_display):
        if self._enable_local_display is True:
            self._local_display = local_display
        else:
            self._local_display = None

    def get_local_display(self):
        return self._local_display

    def set_interface(self, interface):
        if self._interface is True:
            self._interface = interface
        else:
            self._interface = None

    def get_interface(self):
        return self._interface

    def reset_player_ids(self):
        self._player_ids = 0
