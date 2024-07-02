from abc import ABC, abstractmethod


class Socket(ABC):
    @abstractmethod
    def plug_in(self):
        pass

    @abstractmethod
    def plug_out(self):
        pass
