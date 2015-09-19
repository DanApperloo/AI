__author__ = 'Dan Apperloo'
__email__ = "danapperloo@gmail.com"


#########################################################################
# Imports
#########################################################################
from abc import ABCMeta
from abc import abstractmethod
from game.behaviour_base import BaseBehaviour
from game.simple_shooter.shooter_game import ShooterGame


#########################################################################
# Functions
#########################################################################
class PlayerBase(BaseBehaviour):

    __metaclass__ = ABCMeta

    def __init__(self, behaviour_id):
        BaseBehaviour.__init__(self, behaviour_id)
        self.interface = None
        self.int_id = None

    def set_interface(self, interface_obj, interface_id):
        self.interface = interface_obj
        self.int_id = interface_id
        return

    @abstractmethod
    def set_initial_conditions(self, x_pos, y_pos, rot):
        pass

    @abstractmethod
    def update_move(self):
        pass

    @abstractmethod
    def update_action(self):
        pass