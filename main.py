__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'


#########################################################################
# Imports
#########################################################################
from example.example_rps_game import RPSGame
from example.example_rps_behaviour_base import RPSBaseBehaviour
from control.behaviour_control import BehaviourBuilder


#########################################################################
# Functions
#########################################################################
if __name__ == "__main__":

    # Load the Behaviour Builder
    behaviour_builder = BehaviourBuilder(RPSBaseBehaviour,
                                         "./test_scripts/example_rps/",
                                         [])

    try:
        bhv = behaviour_builder.get_behaviour_indexes_by_name(["test_ai_1.py",
                                                               "test_ai_2.py"])

        # Ensure Valid scripts for test
        for ai in bhv:
            assert ai.secure is True

        # Run the Game
        results = []
        for i in range(0, 10):
            for ai in bhv:
                if ai.obj is not None:
                    ai.obj.determine_move()

            results.append(RPSGame.calculate_result())

            for ai in bhv:
                if ai.obj is not None:
                    ai.obj.update_state(results[i])

        # Print the Results
        print "Printing Results"
        for game in results:
            print game
        print ''

        # Perform Clean Up
        behaviour_builder.cleanup()

    except Exception as e:
        # Perform Clean Up
        behaviour_builder.cleanup()
        raise
