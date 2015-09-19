from simple_shooter.user_reference import player_base

__author__ = 'Dan Apperloo'
__email__ = "danapperloo@gmail.com"


#########################################################################
# Imports
#########################################################################
from game.game_index import GameIndex
from game.example import example_rps_behaviour_base, example_rps_game
from game.simple_shooter import shooter_game


#########################################################################
# Functions
#########################################################################
class GameControl(object):

    GAME_INDEX = {
        'Rock-Paper-Scissors': GameIndex(example_rps_behaviour_base.RPSBaseBehaviour,
                                         './test_scripts/example_rps/',
                                         example_rps_game.RPSGame),
        'Simple-Shooter': GameIndex(player_base.PlayerBase,
                                    './test_scripts/simple_shooter/',
                                    shooter_game.ShooterGame)
    }

    @staticmethod
    def get_game_index(game_id):
        return GameControl.GAME_INDEX[game_id]
