__author__ = 'Dan Apperloo'
__email__ = "danapperloo@gmail.com"


#########################################################################
# Imports
#########################################################################
import os
import re
import sys
import shutil
import fnmatch
import inspect
import config.common as common
from behaviour_index import BehaviourIndex


#########################################################################
# Functions
#########################################################################
class BehaviourControl(object):

    INDEX_REGEX = '*.py'

    VALIDATION_PREFIX = "vld_"
    VALIDATION_PREFIX_REGEX = "^vld.*"
    VALIDATION_DIRECTORY = "./staging/"

    MODULE_PREFIX = "staging."

    ID_GENERATOR = 0

    BASIC_BANNED_API = ["\s*import\s*os"]

    def __init__(self, base_class, entry_path, banned_api):
        self.comparison_base_class = base_class
        self.entry_path = entry_path
        self.behaviour_index_list = []

        # Remove any repeats to reduce processing time
        for x in self.BASIC_BANNED_API:
            try:
                banned_api.remove(x)
            except ValueError:
                continue
        self.specific_banned_api = banned_api

        # Perform some initial cleanup, just in case
        self._remove_all_validated_scripts()

        # Generate initial index
        self._generate_index()
        return

    def _generate_index(self):
        """
        Generate Behaviour Index objects for scripts in a given folder.

        :return: nothing
        """
        # Iterate through a given directory and generate a Behaviour Index List
        for file_name in os.listdir(self.entry_path):
            if fnmatch.fnmatch(file_name, self.INDEX_REGEX):
                self.behaviour_index_list.append(BehaviourIndex(self.entry_path,
                                                 file_name))
        return

    def regenerate_index(self):
        """
        Regenerates the Behaviour Index.

        :return: nothing
        """
        self.behaviour_index_list = []
        self._remove_all_validated_scripts()
        self._generate_index()
        return

    def get_behaviour_indexes_by_name(self, behaviour_name_list):
        """
        Return the behaviour indexes for the file names given.

        :param behaviour_name_list: list of behaviour file names
        :return: list of requested behavior indexes
        """
        requested_behaviours = self._find_behaviours(behaviour_name_list)
        try:
            self._validate_behaviours(requested_behaviours)
            self._load_behaviours(requested_behaviours)
        except (RuntimeError, IOError) as e:
            print "Exception ({0}): {1}".format(e.errno, e.strerror)
            self._remove_all_validated_scripts()
            raise
        return requested_behaviours

    def instantiate_behaviours(self, behaviours):
        """
        Instantiate the desired behaviours if possible.

        :param behaviours: list of behaviour indexes
        :return: nothing
        """
        for index in behaviours:
            # Attempt to reload the error
            if index.missing is False:
                if index.secure is True:
                    if index.loaded is False:
                        if index.constructor is not None:
                            index.obj = index.constructor(self.ID_GENERATOR)
                            self.ID_GENERATOR += 1
                            index.loaded = True
                            index.status = BehaviourIndex.STATUS_SUCCESS

            # If desired index wasn't loaded, set RELOAD Error
            if index.loaded is False:
                index.status = BehaviourIndex.STATUS_RELOAD_ERROR
        return

    def cleanup(self):
        """
        Removes any validation scripts and unload behaviours.

        :return: Nothing
        """
        self._unload_all_behaviours()
        self._remove_all_validated_scripts()
        return

    def _find_behaviours(self, behaviours_to_find_by_name):
        """
        Find the behaviour index objects by filename.

        :param behaviours_to_find_by_name: list of file names
        :return: list of behaviour indexes
        """
        # Find the behaviour indexes associated with script names
        behaviours = []
        for index in self.behaviour_index_list:
            if index.file_name in behaviours_to_find_by_name:
                index.status = BehaviourIndex.STATUS_SUCCESS
                behaviours.append(index)
                behaviours_to_find_by_name.remove(index.file_name)

        # Check if any script names aren't found
        if len(behaviours_to_find_by_name) is not 0:
            for script in behaviours_to_find_by_name:
                if common.DEBUG:
                    print "Unable to find index for " + script
                    print "Generating an index and labeling as invalid..."

                invalid_index = BehaviourIndex(self.entry_path, script)
                invalid_index.missing = True
                invalid_index.status = BehaviourIndex.STATUS_MISSING
                self.behaviour_index_list.append(invalid_index)
                behaviours.append(invalid_index)
        return behaviours

    def _validate_behaviours(self, behaviour_indexes):
        """
        Examine the Indexed Behaviours for any Banned APIs.

        :param behaviour_indexes: a list of Behaviours to validate
        :return: nothing
        """
        # Loop through given Indices
        for index in behaviour_indexes:

            if index.missing is False:
                # Open the file and search for
                file_under_test = open(index.file_dir + index.file_name, 'r')
                print file_under_test
                insecure_call_found = False
                for line in file_under_test:
                    for basic_banned_api in self.BASIC_BANNED_API:
                        if re.search(basic_banned_api, line) is not None:
                            if common.DEBUG:
                                print "Insecure call: " + basic_banned_api + " found in " + index.file_name
                            insecure_call_found = True
                    for specific_banned_api in self.specific_banned_api:
                        if re.search(specific_banned_api, line) is not None:
                            if common.DEBUG:
                                print "Insecure call: " + specific_banned_api + " found in " + index.file_name
                            insecure_call_found = True

                # Ensure the flags are set accordingly
                if insecure_call_found is False:
                    index.secure = True
                else:
                    index.status = BehaviourIndex.STATUS_INVALID

                # Copy a the script to the validated folder for loading
                if index.secure is True:
                    validated_script_name = self.VALIDATION_PREFIX + index.file_name
                    shutil.copy2(index.file_dir + index.file_name, self.VALIDATION_DIRECTORY + validated_script_name)
                    index.validation_file = validated_script_name
                    index.status = BehaviourIndex.STATUS_SUCCESS

                    if common.DEBUG:
                        print "Script Validated: " + index.file_dir + index.file_name
                else:
                    index.status = BehaviourIndex.STATUS_INVALID
                    if common.DEBUG:
                        print "Banned API found in: " + index.file_dir + index.file_name
        return

    def _load_behaviours(self, behaviour_indexes):
        """
        Load Scripts as modules and inspect the contents for
        a Behaviour Subclass to instantiate.

        :param behaviour_indexes: a list of Behaviours to load
        :return: a list of instantiated Behaviours
        """
        # Loop through given scripts
        for index in behaviour_indexes:

            if index.secure is True:
                # Import Script and generate module object
                module = self.MODULE_PREFIX + index.validation_file.split('.')[0]
                __import__(module)
                ai_module = sys.modules[module]

                # For each element in the module object, check if it is a Behaviour
                for name, obj in inspect.getmembers(ai_module):

                    # Check if any classes are Behaviour Subclasses
                    if inspect.isclass(obj):
                        # Prevents getting a hit on the import of the base class or base class instantiation
                        if not inspect.isabstract(obj):
                            if BehaviourControl.__inherits_from(obj, self.comparison_base_class.__name__):
                                # Log details about script
                                if common.DEBUG:
                                    print "Behaviour Class:  " + str(name)
                                    print "Behaviour Object: " + str(obj)

                                # Set the found class obj into the behaviour index
                                index.constructor = obj
                                index.loaded = True
                                index.obj = index.constructor(self.ID_GENERATOR)
                                index.status = BehaviourIndex.STATUS_SUCCESS
                                self.ID_GENERATOR += 1
                                break

                # If no Behaviour was found, append a None to the list
                if index.loaded is False:
                    index.status = BehaviourIndex.STATUS_LOAD_ERROR
                    print "Error: Script does not Subclass Behaviour API. File: " + str(ai_module)
        return

    def _unload_all_behaviours(self):
        """
        Unload and free any loaded behaviours.

        :return: nothing
        """
        for index in self.behaviour_index_list:
            if index.loaded is True:
                del index.obj
                index.loaded = False
        return

    def _remove_all_validated_scripts(self):
        """
        Clean up copies of validated scripts.

        :return: nothing
        """
        # Iterate through the Validated directory and cleanup script copies
        for filename in os.listdir(self.VALIDATION_DIRECTORY):
            if re.search(self.VALIDATION_PREFIX_REGEX, filename):
                os.remove(os.path.join(self.VALIDATION_DIRECTORY, filename))
        return

    @staticmethod
    def __inherits_from(child, parent_name):
        """
        Uses inspect to determine if class is a desired sub class.
        This could be circumvented but the combination of using ABC class for abstraction
        highly mitigates possible damage.

        :param child: object to test
        :param parent_name: name of desired parent class
        :return: True if child is subclassing parent_name, false otherwise
        """
        if inspect.isclass(child):
            if parent_name in [parent.__name__ for parent in inspect.getmro(child)[1:]]:
                return True
        return False
