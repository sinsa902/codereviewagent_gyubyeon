from unittest import TestCase
from refact1 import split_and_sum


class Test(TestCase):
    def test_split_and_sum(self):
        ret = split_and_sum("0-1-2-3-4")
        self.assertEqual(10, ret)
