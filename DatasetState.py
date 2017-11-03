#
#
#  Author: Amar Debnath, Roll: 23
#
#


import abc

class DatasetState(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getCSVData(self):
        pass

