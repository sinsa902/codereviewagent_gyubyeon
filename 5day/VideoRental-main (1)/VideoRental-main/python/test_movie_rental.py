from unittest import TestCase
from customer import Customer, Rental, Movie
from bill import New_Bill, Regular_Bill, Children_Bill

TITLE = "TITLE_NOT_IMPORTANT"

CUSTOMER_NAME = "NAME_NOT_IMPORTANT"


class Tests(TestCase):
    def setUp(self):
        super().setUp()
        self.customer = Customer(CUSTOMER_NAME)

    def test_sample(self):
        self.assertIsNotNone(self.customer)

    def test_sta(self):
        statement = self.customer.statement()
        expected = """Rental Record for NAME_NOT_IMPORTANT
Amount owed is 0.0
You earned 0 frequent renter points"""
        self.assertEqual(expected, statement)

    def test_sta2(self):
        days_rented = 2
        self.add_cart_regular(days_rented)
        expected = """Rental Record for NAME_NOT_IMPORTANT
	TITLE_NOT_IMPORTANT	2.0
Amount owed is 2.0
You earned 1 frequent renter points"""
        self.assertEqual(self.customer.statement(), expected)

    def test_sta3(self):
        days_rented = 1
        self.add_cart_new(days_rented)
        expected = """Rental Record for NAME_NOT_IMPORTANT
	TITLE_NOT_IMPORTANT	3.0
Amount owed is 3.0
You earned 1 frequent renter points"""
        self.assertEqual(self.customer.statement(), expected)

    def add_cart_new(self, days_rented):
        rental = self.__create_rental(days_rented, Movie.NEW_RELEASE)
        self.customer.add_rental(rental)
        self.customer.add_bill(New_Bill(rental))

    def test_sta4(self):
        days_rented = 4
        self.add_cart_child(days_rented)
        expected = """Rental Record for NAME_NOT_IMPORTANT
	TITLE_NOT_IMPORTANT	3.0
Amount owed is 3.0
You earned 1 frequent renter points"""
        self.assertEqual(self.customer.statement(), expected)

    def add_cart_child(self, days_rented):
        rental = self.__create_rental(days_rented, Movie.CHILDRENS)
        self.customer.add_rental(rental)
        self.customer.add_bill(Children_Bill(rental))

    def test_sta5(self):
        days_rented = 3
        self.add_cart_child(days_rented)
        expected = """Rental Record for NAME_NOT_IMPORTANT
	TITLE_NOT_IMPORTANT	1.5
Amount owed is 1.5
You earned 1 frequent renter points"""
        self.assertEqual(self.customer.statement(), expected)

    def test_sta6(self):
        days_rented = 2
        self.add_cart_new(days_rented)
        expected = """Rental Record for NAME_NOT_IMPORTANT
	TITLE_NOT_IMPORTANT	6.0
Amount owed is 6.0
You earned 2 frequent renter points"""
        self.assertEqual(self.customer.statement(), expected)

    def test_sta7(self):
        self.add_cart_regular(1)
        self.add_cart_new(4)
        self.add_cart_child(4)

        expected = """Rental Record for NAME_NOT_IMPORTANT
	TITLE_NOT_IMPORTANT	2.0
	TITLE_NOT_IMPORTANT	12.0
	TITLE_NOT_IMPORTANT	3.0
Amount owed is 17.0
You earned 4 frequent renter points"""
        self.assertEqual(self.customer.statement(), expected)

    def test_t1(self):
        Movie.set_price_code(self, 10)
        days_rented = 2
        self.add_cart_new(days_rented)
        expected = """Rental Record for NAME_NOT_IMPORTANT
	TITLE_NOT_IMPORTANT	6.0
Amount owed is 6.0
You earned 2 frequent renter points"""
        self.assertEqual(self.customer.statement(), expected)

    def test_t2(self):
        days_rented = 5
        self.add_cart_regular(days_rented)
        expected = """Rental Record for NAME_NOT_IMPORTANT
	TITLE_NOT_IMPORTANT	6.5
Amount owed is 6.5
You earned 1 frequent renter points"""
        self.assertEqual(self.customer.statement(), expected)

    def __create_rental(self, days_rented, price_code):
        movie = Movie(TITLE, price_code)
        rental = Rental(movie, days_rented)
        return rental

    def add_cart_regular(self, days_rented):
        rental = self.__create_rental(days_rented, Movie.REGULAR)
        self.customer.add_rental(rental)
        self.customer.add_bill(Regular_Bill(rental))
