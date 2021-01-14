from abc import abstractmethod, ABCMeta
import datetime
import queue

import numpy as np
import pandas as pd

from event import SignalEvent

class Strategy(object):
    """
    Strategy is an abstract base class providing interface for all subsequent strategy handling objects.

    The goal of a Strategy object is to generate Signal objects for particular symbols based on the inputs of
    Bars generated by a DataHandler objects.

    This is designed to work both with historic and live data as the Strategy object is agnostic to where the data
    came from, since it obtains the bar tuples from a queue object.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def calc_signals(self, *args, **kwargs):
        """
        Provides the mechanisms to calculate the list of signals.
        """
        raise NotImplementedError("Should implement calculate_signals()")

#Startegy 추가해 나가면 됨