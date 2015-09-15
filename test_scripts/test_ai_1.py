from game import rock_paper_scissors as RPS, behaviour_base

__author__ = 'Dan'


class test(behaviour_base.AIBase):

    def __init__(self, ai_id):
        super(test, self).__init__(ai_id)
        print "Test AI 1 " + str(ai_id)

    def initialize(self):
        print "Test AI 1 initialize"

    def determine_move(self):
        print "Test AI 1 determine move"
        RPS.RPSGame.submit_move(self.obj_id, RPS.State.Rock)

    def update_state(self, last_state):
        print "Test AI 1 update state"