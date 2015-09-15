from game import rock_paper_scissors as RPS, behaviour_base

__author__ = 'Dan'


class test_C(behaviour_base.AIBase):

    def __init__(self, ai_id):
        super(test_C, self).__init__(ai_id)
        print "Test AI 2 " + str(ai_id)

    def initialize(self):
        print "Test AI 2 initialize"

    def determine_move(self):
        print "Test AI 2 determine move"
        RPS.RPSGame.submit_move(self.obj_id, RPS.State.Paper)

    def update_state(self, last_state):
        print "Test AI 2 update state"