# sort print machine
from abc import ABC, abstractmethod


class Sort(ABC):
    @abstractmethod
    def do_srt(self, lst):
        pass


# test
class SelectionSort(Sort):
    def do_srt(self, lst):
        pass
