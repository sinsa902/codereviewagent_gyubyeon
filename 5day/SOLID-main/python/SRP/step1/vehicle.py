class fuel:
    def __init__(self, max_fuel):
        self.__max_fuel = max_fuel
        self.__remain_fuel = max_fuel

    def re_fuel(self):
        self.__remain_fuel = self.__max_fuel

    def get_max_fuel(self):
        return self.__max_fuel

    def set_remaing_fuel(self):
        return self.__remain_fuel

    def decrease(self, amount):
        if self.__remain_fuel - amount < 0:
            print("no fuel anymore")
            return
        self.__remain_fuel -= 1


class Vehicle:
    def __init__(self, fuel: fuel) -> None:
        super().__init__()
        self.fuel = fuel

    def accelerate(self):
        self.fuel.decrease(1)
