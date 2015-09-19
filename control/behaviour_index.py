__author__ = 'Dan Apperloo'
__email__ = "danapperloo@gmail.com"


#########################################################################
# Functions
#########################################################################
class BehaviourIndex(object):

    STATUS_SUCCESS = 0
    STATUS_LOAD_ERROR = -1
    STATUS_MISSING = -2
    STATUS_INVALID = -3
    STATUS_RELOAD_ERROR = -4

    def __init__(self, file_directory, file_name):
        self.file_dir = file_directory
        self.file_name = file_name
        self.validation_file = None
        self.constructor = None
        self.obj = None
        self.secure = False
        self.loaded = False
        self.missing = False
        self.status = self.STATUS_SUCCESS
        return