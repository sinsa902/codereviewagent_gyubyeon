import unittest
from getAbsoluteSum import getAbsoluteSum


class TestAddFunction(unittest.TestCase):

    def test_add_zero(self):
        self.assertEqual(getAbsoluteSum([-1, -1]), [1, 1])


if __name__ == "__main__":
    unittest.main()
