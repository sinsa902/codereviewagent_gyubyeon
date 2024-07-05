from abc import ABC, abstractmethod


class ABC_Bill(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def make_bill(self):
        pass

    @abstractmethod
    def _set_freq(self):
        pass

    @abstractmethod
    def _set_amount(self):
        pass

    @abstractmethod
    def _set_texts(self):
        pass

    @abstractmethod
    def get_texts(self):
        pass

    @abstractmethod
    def get_amount(self):
        pass

    @abstractmethod
    def get_freq(self):
        pass


class Bill(ABC_Bill):
    def __init__(self, rental):
        self._days_rented = rental.get_days_rented()
        self._movie = rental.get_movie()
        self._freq = 0
        self._amount = 0
        self._texts = ""

    def make_bill(self):
        self._set_amount()
        self._set_freq()
        self._set_texts()

    def _set_freq(self):
        pass

    def _set_amount(self):
        pass

    def _set_texts(self):
        self._texts = (
            "\t"
            + self._movie.get_title()
            + "\t"
            + str(
                f"{self._amount:.1f}",
            )
            + "\n"
        )

    def get_texts(self):
        return self._texts

    def get_amount(self):
        return self._amount

    def get_freq(self):
        return self._freq


class Regular_Bill(Bill):
    def __init__(self, rental):
        super().__init__(rental)
        self.make_bill()

    def _set_freq(self):
        self._freq = 1

    def _set_amount(self):
        self._amount = 2.0
        if self._days_rented > 2:
            self._amount += (self._days_rented - 2) * 1.5


class New_Bill(Bill):
    def __init__(self, rental):
        super().__init__(rental)
        self.make_bill()

    def _set_freq(self):
        self._freq = 1
        if self._days_rented > 1:
            self._freq += 1

    def _set_amount(self):
        self._amount = self._days_rented * 3


class Children_Bill(Bill):
    def __init__(self, rental):
        super().__init__(rental)
        self.make_bill()

    def _set_freq(self):
        self._freq = 1

    def _set_amount(self):
        self._amount = 1.5
        if self._days_rented > 3:
            self._amount += (self._days_rented - 3) * 1.5
