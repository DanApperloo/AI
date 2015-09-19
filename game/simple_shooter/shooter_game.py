__author__ = 'Dan Apperloo'
__email__ = "danapperloo@gmail.com"


#########################################################################
# Imports
#########################################################################
import uuid
from game.simple_shooter.shooter_game_interface import IShooterGame


#########################################################################
# Functions
#########################################################################
class ShooterGame(object):

    def __init__(self):
        self.interface = IShooterGame()
        self.players_map = {}
        self.move_sub_map = {}
        self.action_sub_map = {}
        return

    def set_players(self, player_list):
        for player in player_list:
            # Generate a UUID to use as a submission key
            uid = uuid.uuid4()
            player.set_interface(self.interface, uid)
            self.players_map[uid] = player

    def set_initial(self):
        # For each player, set a starting point and orientation
        return

    def game_loop(self):
        # Physic calculation/collision
        # Input management
        # Move determination
        # Action determination
        # New state / Render
        return