from abc import ABC, abstractmethod

from movie import Movie


class ABC_Rental(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_days_rented(self):
        pass

    @abstractmethod
    def get_movie(self):
        pass


class Rental(ABC_Rental):
    def __init__(self, movie: Movie, daysRented: int):
        self.__days_rented = daysRented
        self.__movie = movie

    def get_days_rented(self):
        return self.__days_rented

    def get_movie(self):
        return self.__movie
