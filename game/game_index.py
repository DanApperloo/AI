__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'


#########################################################################
# Imports
#########################################################################


#########################################################################
# Functions
#########################################################################
class GameIndex(object):

    def __init__(self, base_class, sub_dir, game_con):
        self.behaviour_base_class = base_class
        self.behaviour_sub_dir = sub_dir
        self.game_constructor = game_con