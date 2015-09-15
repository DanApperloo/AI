__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'

#########################################################################
# Imports
#########################################################################
import sys
import inspect
import config.common as common
from game import behaviour_base


#########################################################################
# Functions
#########################################################################
def load_behaviours(behaviour_scripts):
    """
    Load Scripts as modules and inspect the contents for
    a Behaviour Subclass to instantiate.

    :param behaviour_scripts: a list of Behaviour file names
    :return: a list of instantiated Behaviours
    """

    # Local Variables
    subclass_list = []
    file_list = []
    behaviour_list = []

    # Loop through given scripts
    for script in behaviour_scripts:
        # Iteration Variables
        iter_found_behaviour = False

        # Import Script and generate module object
        module = "staging." + script.split('.')[0]
        __import__(module)
        ai_module = sys.modules[module]
        file_list.append(ai_module)

        # For each element in the module object, check if it is a Behaviour
        for name, obj in inspect.getmembers(ai_module):

            # Check if any classes are Behaviour Subclasses
            if inspect.isclass(obj):
                if issubclass(obj, behaviour_base.BaseBehaviour):

                    # Log details about script
                    if common.DEBUG:
                        print "Behaviour Class:  " + str(name)
                        print "Behaviour Object: " + str(obj)

                    # Append the class to our Behaviours List
                    subclass_list.append(obj)

                    # We found a valid Behaviour, so load next script
                    iter_found_behaviour = True
                    break

        # If no Behaviour was found, append a None to the list
        if iter_found_behaviour is False:
            print "Error: Script does not Subclass Behaviour API. File: " + str(ai_module)
            subclass_list.append(None)

    # Log loaded Behaviours
    if common.DEBUG:
        print "Behaviour Scripts: " + str(file_list)
        print "Behaviour Objects: " + str(subclass_list)

    # Initialize the Objects
    iter_count = 0
    for obj in subclass_list:
        if obj is not None:
            behaviour_list.append(obj(iter_count))
        else:
            behaviour_list.append(None)
        iter_count += 1

    # Returns the List of initialized Behaviour Objects
    return behaviour_list
