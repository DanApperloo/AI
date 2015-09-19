__author__ = 'Dan Apperloo'
__email__ = "danapperloo@gmail.com"


#########################################################################
# Imports
#########################################################################
from abc import ABCMeta
from abc import abstractmethod
from game.behaviour_base import BaseBehaviour


#########################################################################
# Functions
#########################################################################
class RPSBaseBehaviour(BaseBehaviour):

    __metaclass__ = ABCMeta

    def __init__(self, behaviour_id):
        BaseBehaviour.__init__(self, behaviour_id)

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def determine_move(self):
        pass

    @abstractmethod
    def update_state(self, last_result):
        pass