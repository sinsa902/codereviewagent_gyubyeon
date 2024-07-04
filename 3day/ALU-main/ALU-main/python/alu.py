from alu_result import ALU_result


class ALU:
    def __init__(self) -> None:
        super().__init__()
        self.operand1 = -1
        self.operand2 = -1
        self.opcode = ""

    def set_operand1(self, operand1):
        self.operand1 = operand1

    def set_operand2(self, operand2):
        self.operand2 = operand2

    def set_opcode(self, opcode):
        self.opcode = opcode

    def enable_signal(self, r: ALU_result):
        if not self.__is_valid1(r):
            return
        if not self.__is_valid2():
            return

        self.__get_operation(r)

    def __get_operation(self, r):
        result = {
            "ADD": self.operand1 + self.operand2,
            "MUL": self.operand1 * self.operand2,
            "SUB": self.operand1 - self.operand2,
        }.get(self.opcode, None)
        r.set_result(result)
        r.set_status(0)

    def __is_valid1(self, r):
        if not self.opcode in ["ADD", "MUL", "SUB"]:
            self.__set_errorcode(3)
            return False
        return True

    def __is_valid2(self):
        if self.operand1 == -1:
            self.__set_errorcode(1)
            return False

        if self.operand2 == -1:
            self.__set_errorcode(2)
            return False
        return True

    def __set_errorcode(self, error_code):
        r.set_result(65535)
        r.set_status(error_code)
