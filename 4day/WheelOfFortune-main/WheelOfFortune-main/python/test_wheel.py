from unittest import TestCase

from wheel import get_award


class Test(TestCase):
    def test_get_award1(self):
        board = [list("BUILDLEV"), list("EATREALROBOT")]
        user_input = "ERABCDFGHIJKLMNOPQSTUVWXYZ"

        self.assertEqual(get_award(2, board, user_input), "$6500")

    def test_get_award2(self):
        board = [list("ABS"), list("ABS"), list("AAAAAKBA")]
        user_input = "XASBKQDJHMNPTLVUCGEWFORIYZ"

        self.assertEqual(get_award(3, board, user_input), "$9500")
