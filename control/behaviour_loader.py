from game import behaviour_base as AI

__author__ = 'Dan'

import sys
import inspect


def gather_ais(ai_scripts):
    subclass_list = []
    file_list = []

    for script in ai_scripts:
        module = "test_scripts." + script.split('.')[0]
        __import__(module)
        ai_module = sys.modules[module]
        file_list.append(ai_module)

        for name, obj in inspect.getmembers(ai_module):
            if inspect.isclass(obj):
                ## Class Name
                print name
                ## Object Structure
                print obj

                if issubclass(obj, AI.AIBase):
                    print "Is Subclass"
                    subclass_list.append(obj)
                else:
                    print "AI is not Subclass in Module " + str(ai_module)
                    continue

    print "AI Scripts"
    print file_list
    print ''

    # Initialize the Objects
    ai_list = []
    ai_list.append(subclass_list[0](0))
    ai_list.append(subclass_list[1](1))

    return ai_list