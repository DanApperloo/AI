__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'


#########################################################################
# Imports
#########################################################################
from game.simple_shooter.user_reference.player_base import PlayerBase


#########################################################################
# Functions
#########################################################################
class TestA(PlayerBase):

    def __init__(self, behaviour_id):
        PlayerBase.__init__(self, behaviour_id)
        print "Test AI 1 " + str(behaviour_id)

    def set_initial_conditions(self, x_pos, y_pos, rot):
        pass

    def update_move(self):
        pass

    def update_action(self):
        pass