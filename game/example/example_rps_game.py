__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'


#########################################################################
# Functions
#########################################################################
class State:
    Rock = 0
    Paper = 1
    Scissors = 2

    def __init__(self):
        pass


class Outcome:
    Loss = 0
    Tie = 1
    Win = 2

    def __init__(self):
        pass


class RPSGame(object):
    player_1_input = None
    player_2_input = None

    def __init__(self):
        self.players = None
        return

    def set_players(self, player_list):
        self.players = player_list

    def start(self):

        results = []
        for i in range(0, 10):
            for player in self.players:
                player.determine_move()

            results.append(RPSGame.calculate_result())

            for player in self.players:
                player.update_state(results[i])

        # Print the Results
        print "Printing Results"
        for game in results:
            print game
        return

    @classmethod
    def submit_move(cls, ai_id, state):
        if ai_id == 1:
            cls.player_1_input = state
        else:
            cls.player_2_input = state

    @classmethod
    def calculate_result(cls):
        if cls.player_1_input == cls.player_2_input:
            return [Outcome.Tie, Outcome.Tie]
        if (cls.player_1_input == State.Rock) and (cls.player_2_input == State.Paper):
            return [Outcome.Loss, Outcome.Win]
        if (cls.player_1_input == State.Rock) and (cls.player_2_input == State.Scissors):
            return [Outcome.Win, Outcome.Loss]
        if (cls.player_1_input == State.Paper) and (cls.player_2_input == State.Scissors):
            return [Outcome.Loss, Outcome.Win]
        if (cls.player_1_input == State.Paper) and (cls.player_2_input == State.Rock):
            return [Outcome.Win, Outcome.Loss]
        if (cls.player_1_input == State.Scissors) and (cls.player_2_input == State.Paper):
            return [Outcome.Win, Outcome.Loss]
        if (cls.player_1_input == State.Scissors) and (cls.player_2_input == State.Rock):
            return [Outcome.Loss, Outcome.Win]