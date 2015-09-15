__author__ = 'Dan Apperloo'
__email__ = 'danapperloo@gmail.com'


#########################################################################
# Imports
#########################################################################
import os
import re
import shutil
import config.common as common


#########################################################################
# Functions
#########################################################################
def validate_behaviours(directory_path, behaviour_scripts):
    """

    :param directory_path:
    :param behaviour_scripts:
    :return:
    """

    # Local Variables
    script_status_list = []

    # Loop through given scripts
    for script in behaviour_scripts:
        validated_script_name = "VLD_" + script
        shutil.copy2(directory_path + script, './staging/' + validated_script_name)
        script_status_list.append(validated_script_name)

    return script_status_list


def remove_validated_scripts():
    """

    :return:
    """

    for filename in os.listdir('./staging/'):
        if re.search("^VLD.*", filename):
            os.remove(os.path.join('./staging/', filename))

    return