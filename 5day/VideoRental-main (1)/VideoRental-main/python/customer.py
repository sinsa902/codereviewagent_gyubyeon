from rental import Rental
from movie import Movie
from bill import Bill


class Customer:
    def __init__(self, name: str):
        self.__rentals = []
        self.__name = name
        self.__bills = []

    def get_name(self):
        return self.__name

    def statement(self):
        frequent_renter_points, texts, total_amount = self._summary_bills()
        result = self._printout_bill(frequent_renter_points, texts, total_amount)

        return result

    def _printout_bill(self, frequent_renter_points, texts, total_amount):
        result = str()
        result += "Rental Record for " + self.get_name() + "\n"
        result += texts
        result += "Amount owed is " + f"{total_amount}" + "\n"
        result += (
            "You earned " + str(frequent_renter_points) + " frequent renter points"
        )
        return result

    def _summary_bills(self):
        total_amount = 0.0
        frequent_renter_points = 0
        texts = ""
        for this_bill in self.__bills:
            total_amount += this_bill._amount
            frequent_renter_points += this_bill._freq
            texts += this_bill._texts
        return frequent_renter_points, texts, total_amount

    def add_rental(self, param: Rental):
        self.__rentals.append(param)

    def add_bill(self, bill: Bill):
        if not isinstance(bill, Bill):
            return print("Bill class needed")
        self.__bills.append(bill)
