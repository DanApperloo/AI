__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'


#########################################################################
# Imports
#########################################################################
from game.simple_shooter.user_reference.player_base import PlayerBase


#########################################################################
# Functions
#########################################################################
class TestB(PlayerBase):

    def __init__(self, behaviour_id):
        PlayerBase.__init__(self, behaviour_id)
        print "Test AI 2 " + str(behaviour_id)

    def set_initial_conditions(self, x_pos, y_pos, rot):
        pass

    def update_move(self):
        pass

    def update_action(self):
        pass