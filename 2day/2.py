class Calculator:
    def __init__(self) -> None:
        print("초기화 완료")
        self.__result = 0

    def plus(self, x1, x2):
        self.__result = x1 + x2

    def minus(self, x1, x2):
        self.__result = x1 - x2

    def divide(self, x1, x2):
        try:
            self.__result = x1 / x2
        except Exception as e:
            print(f"error 발생 {e}")
            self.__result = None

    def multiple(self, x1, x2):
        self.__result = x1 * x2

    def print__result(self):
        print(f"결과물: {self.__result}")
        self.__init__()


c1 = Calculator()
c1.plus(1, 5)
c1.print__result()
c1.divide(5, 0)
c1.__result
