from unittest import TestCase
from unittest.mock import Mock, call, patch

from calc import Calc


class TestCalc(TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_cal(self):
        self.assertEqual(1, 1)
        mk = Mock(spec=Calc)
        mk.get_sum.return_value = 10
        self.assertEqual(10, mk.get_sum(mk))
        mk.assert_not_called()

    def test_cal2(self):
        mk = Mock()
        mk.test.return_value = 1000
        mk.run.return_value = 2000

        print(mk.test(1, 2))
        print(mk.test(1, 4))
        print(mk.test(5, 2))

        print(mk.run(1, 1, 1, 1))
        mk.run.assert_called_once()
        mk.test.assert_any_call(1, 2)
        mk.test.assert_called_with(5, 2)
        mk.test.assert_has_calls([call(1, 2), call(1, 4)])
        self.assertLessEqual(1, mk.test.call_count())

    @patch.object(Calc, "test")
    def test_cal3(self, test1):
        test1.return_value = 10
        c = Calc()
        print(c.test())
