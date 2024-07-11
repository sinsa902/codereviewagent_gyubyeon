from unittest import TestCase
from Roman import Roman


class TestRoman(TestCase):
    def converter(self, roman_num: str) -> int:
        rst = self.roman.convert(roman_num)
        return rst

    def setUp(self):
        self.roman = Roman()

    def test_case1(self):
        rst = self.converter("x")
        self.assertEqual(rst, 1)
