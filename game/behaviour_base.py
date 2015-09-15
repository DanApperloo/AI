__author__ = 'Dan'

from abc import ABCMeta, abstractmethod


class AIBase():

    __metaclass__ = ABCMeta

    def __init__(self, ai_id):
        self.obj_id = ai_id

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def determine_move(self):
        pass

    @abstractmethod
    def update_state(self, last_result):
        pass