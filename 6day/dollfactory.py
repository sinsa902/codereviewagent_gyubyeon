from abc import ABC, abstractmethod


class Doll(ABC):
    @abstractmethod
    def __init__(self) -> object:
        self.doll = "BASIC"

    @abstractmethod
    def push(self):
        print(f"{self.doll}")


class RedDoll(Doll):
    def __init__(self) -> object:
        super().__init__()
        self.doll = "RED"


class BlueDoll(Doll):
    def __init__(self) -> object:
        super().__init__()
        self.doll = "BLUE"
