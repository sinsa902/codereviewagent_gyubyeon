class ALU_result:
    def __init__(self) -> None:
        super().__init__()
        self.status = -1
        self.result = 65535

        #status -1 : 결과 안나옴
        #status 0 : 성공
        #status 1 : Operand1이 잘못됨
        #status 2 : Operand2가 잘못됨
        #status 3 : OPCODE가 잘못되었음

    def set_status(self, status):
        self.status = status

    def set_result(self, result):
        self.result = result

    def get_status(self):
        return self.status

    def get_result(self):
        return self.result

