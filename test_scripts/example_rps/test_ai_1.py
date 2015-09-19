__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'


#########################################################################
# Imports
#########################################################################
from example.example_rps_game import RPSGame, State
from example.example_rps_behaviour_base import RPSBaseBehaviour


#########################################################################
# Functions
#########################################################################
class TestA(RPSBaseBehaviour):

    def __init__(self, behaviour_id):
        RPSBaseBehaviour.__init__(self, behaviour_id)
        print "Test AI 1 " + str(behaviour_id)

    def initialize(self):
        print "Test AI 1 initialize"

    def determine_move(self):
        print "Test AI 1 determine move"
        RPSGame.submit_move(self.id, State.Rock)

    def update_state(self, last_state):
        print "Test AI 1 update state"