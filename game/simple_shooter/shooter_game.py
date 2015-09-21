__author__ = 'Dan Apperloo'
__email__ = "danapperloo@gmail.com"


#########################################################################
# Imports
#########################################################################
import uuid
import pygame
from game.game_base import BaseGame
from game.simple_shooter.shooter_game_interface import IShooterGame
from game.simple_shooter.shooter_game_local_display import PygameLocalDisplay


#########################################################################
# Functions
#########################################################################
class ShooterGame(BaseGame):

    def __init__(self):
        BaseGame.__init__(self)

        # Initialize the Clock
        self.clock = pygame.time.Clock()

        # Configure Base Game Flags
        self.enable_local_display()
        # self.enable_replay() # TODO: Implement Replay Frame Saves

        self.set_local_display(PygameLocalDisplay())
        self.set_interface(IShooterGame())

        self.players_map = {}
        self.move_sub_map = {}
        self.action_sub_map = {}
        return

    def set_players(self, behaviour_indexes):
        for index in behaviour_indexes:
            player = index.constructor(self._player_ids)
            self._player_ids += 1

            # Generate a UUID to use as a submission key
            uid = uuid.uuid4()
            player.set_interface(self._interface, uid)
            self.players_map[player.id] = (player, uid)

    def start(self):
        # Perform any setup
        # Run game loop
        while self._local_display.display():
            pass
        return

    def single_loop(self):
        return

    def _set_initial(self):
        # For each player, set a starting point and orientation
        return

    def _game_loop(self):
        # Physic calculation/collision
        # Input management
        # Move determination
        # Action determination
        # New state / Render
        return