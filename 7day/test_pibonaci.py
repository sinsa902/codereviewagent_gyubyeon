import unittest
import pibonaci as pb


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        calc = pb.Calc()
        self.assertEqual(calc.pibonaci(1), 1)  # add assertion here
        self.assertEqual(calc.pibonaci(2), 1)  # add assertion here
        self.assertEqual(calc.pibonaci(3), 2)  # add assertion here
        self.assertEqual(calc.pibonaci(4), 5)  # add assertion here


if __name__ == "__main__":
    unittest.main()
