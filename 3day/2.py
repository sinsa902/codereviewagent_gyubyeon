class OddEven:
    def __init__(self):
        self.__result = []

    def get_result(self, nums):
        self.__result = []
        return self.__result

    def set_result(self, nums):
        ox_result = self.__transform_to_ox(nums)
        self.__result = ox_result

    def __transform_to_ox(self, nums):
        ifelse = {}

    def __kward_oxdict(self, num):
        divide_result = "even" if num % 2 == 0 else "odd"
        ifelse = dict(odd="X", even="O")
        return ifelse.get(divide_result, None)
