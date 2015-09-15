__author__ = 'Dan'


class State:
    Rock = 0
    Paper = 1
    Scissors = 2


class Outcome:
    Loss = 0
    Tie = 1
    Win = 2


class RPSGame:
    player_1_input = None
    player_2_input = None

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