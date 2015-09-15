__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'

from control import behaviour_loader
from game import rock_paper_scissors as RPS


if __name__ == "__main__":
    ais = behaviour_loader.gather_ais(["test_ai_1.py",
                                       "test_ai_2.py",
                                       "test_ai_3.py"])

    results = []
    for i in range(0, 10):
        for ai in ais:
            ai.determine_move()

        results.append(RPS.RPSGame.calculate_result())

        for ai in ais:
            ai.update_state(results[i])

    print "Printing Results"
    for game in results:
        print game
    print ''