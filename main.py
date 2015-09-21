__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'


#########################################################################
# Imports
#########################################################################
from control.behaviour_control import BehaviourControl
from game.game_control import GameControl


#########################################################################
# Functions
#########################################################################
if __name__ == "__main__":

    # Load the desired games index
    game_index = GameControl.get_game_index("Simple-Shooter")
    game_object = game_index.game_constructor()

    # Load the Game's Behaviour Builder
    behaviour_builder = BehaviourControl(game_index.behaviour_base_class,
                                         game_index.behaviour_sub_dir,
                                         [])

    try:
        bhv = behaviour_builder.get_behaviour_indexes_by_name(["test_ai_1.py",
                                                               "test_ai_2.py"])

        # Ensure Valid scripts for test
        for ai in bhv:
            assert ai.loaded is True

        # Set the game players
        game_object.set_players([bhv[0], bhv[1]])

        # Run the Game
        game_object.start()

        # Perform Clean Up
        behaviour_builder.cleanup()

    except Exception as e:
        # Perform Clean Up
        behaviour_builder.cleanup()
        raise
