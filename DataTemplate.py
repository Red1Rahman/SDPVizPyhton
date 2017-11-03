#
#
#  Author: Amar Debnath, Roll: 23
#
#


import abc

class DataTemplate(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getData(self, my_list):
        pass
