from alu_result import ALU_result

class ALU :
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

    def enable_signal(self, r : ALU_result):
        if (self.opcode == "ADD") and (self.opcode != "MUL") and (self.opcode != "SUB") :
            if self.operand1 != -1 and self.operand2 != -1 :
                result = self.operand1 + self.operand2
                r.set_result(result)
                r.set_status(0)
            elif self.operand1 == -1 :
                r.set_result(65535)
                r.set_status(1)
            elif self.operand2 == -1 :
                r.set_result(65535)
                r.set_status(2)
        elif (self.opcode != "ADD") and (self.opcode == "MUL") and (self.opcode != "SUB") :
            if self.operand1 != -1 and self.operand2 != -1 :
                result = self.operand1 * self.operand2
                r.set_result(result)
                r.set_status(0)
            elif self.operand1 == -1 :
                r.set_result(65535)
                r.set_status(1)
            elif self.operand2 == -1 :
                r.set_result(65535)
                r.set_status(2)
        elif (self.opcode != "ADD") and (self.opcode != "MUL") and (self.opcode == "SUB"):
            if self.operand1 != -1 and self.operand2 != -1 :
                result = self.operand1 - self.operand2
                r.set_result(result)
                r.set_status(0)
            elif self.operand1 == -1:
                r.set_result(65535)
                r.set_status(1)
            elif self.operand2 == -1:
                r.set_result(65535)
                r.set_status(2)
        else:
            r.set_result(65535)
            r.set_status(3)
