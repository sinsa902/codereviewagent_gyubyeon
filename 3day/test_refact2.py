from unittest import TestCase
from refact2 import get_result


class Test(TestCase):
    def test_get_result(self):
        self.assertEqual("PASS", get_result("25+61=86"))
