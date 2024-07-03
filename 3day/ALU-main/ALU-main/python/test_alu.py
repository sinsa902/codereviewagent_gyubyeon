from unittest import TestCase
from alu_result import ALU_result
from alu import ALU

class TestALU(TestCase):
    def test_test1(self):
        alu = ALU()
        alu.set_operand1(10)
        alu.set_operand2(20)
        alu.set_opcode("ADD")

        ret = ALU_result()
        alu.enable_signal(ret)

        self.assertEqual(30, ret.get_result())
        self.assertEqual(0, ret.get_status())

