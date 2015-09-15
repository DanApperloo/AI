__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'


#########################################################################
# Imports
#########################################################################
from control import behaviour_loader, behaviour_validator
from game import rock_paper_scissors as rps


#########################################################################
# Functions
#########################################################################
if __name__ == "__main__":

    # Validate the Scripts and move them into staging
    val = behaviour_validator.validate_behaviours("./test_scripts/",
                                                  ["test_ai_1.py",
                                                   "test_ai_2.py"])

    # Load the valid behaviours
    ais = behaviour_loader.load_behaviours(val)

    # Run the Game
    results = []
    for i in range(0, 10):
        for ai in ais:
            if ai is not None:
                ai.determine_move()

        results.append(rps.RPSGame.calculate_result())

        for ai in ais:
            if ai is not None:
                ai.update_state(results[i])

    # Perform Clean Up
    behaviour_validator.remove_validated_scripts()

    # Print the Results
    print "Printing Results"
    for game in results:
        print game
    print ''