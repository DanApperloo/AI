__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'


#########################################################################
# Imports
#########################################################################
from game import rock_paper_scissors as rps, behaviour_base


#########################################################################
# Functions
#########################################################################
class TestA(behaviour_base.BaseBehaviour):

    def __init__(self, ai_id):
        super(TestA, self).__init__(ai_id)
        print "Test AI 1 " + str(ai_id)

    def initialize(self):
        print "Test AI 1 initialize"

    def determine_move(self):
        print "Test AI 1 determine move"
        rps.RPSGame.submit_move(self.obj_id, rps.State.Rock)

    def update_state(self, last_state):
        print "Test AI 1 update state"