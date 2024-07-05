from abc import ABC, abstractmethod

INTIMATE = "intimate"

CASUAL = "casual"

FORMAL = "formal"


class Greeter:
    def __init__(self) -> None:
        super().__init__()

    def greet(self, this: Formality) -> str:
        if not isinstance(this, Formality):
            return "error no Formality type"
        return this.greet()


class ABC_Formality(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def set_formality(self, formality: str):
        pass

    @abstractmethod
    def greet(self):
        pass


class Formality(ABC_Formality):
    def __init__(self):
        self.__formality = ""

    def set_formality(self, formality: str):
        self.__formality = formality

    def greet(self):
        return "Hello."


class Formal_Way(Formality):
    def __init__(self):
        super().__init__()
        self.__formality = FORMAL

    def greet(self):
        return "Good evening, sir."


class Casual_Way(Formality):
    def __init__(self):
        super().__init__()
        self.__formality = CASUAL

    def greet(self):
        return "Sup bro?"


class Intimate_Way(Formality):
    def __init__(self):
        super().__init__()
        self.__formality = INTIMATE

    def greet(self):
        return "Hello Darling!"
