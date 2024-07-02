class Robot:
    def __init__(self) -> None:
        self.__hp = 0

    def move(self):
        pass

    def step(self):
        pass

    def getHp(self):
        return self.__hp


class SpeedRobot(Robot):
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        pass

    def walk(self):
        pass


class PowerRobot(Robot):
    def __init__(self) -> None:
        super().__init__()

    def attack(self):
        pass

    def jump(self):
        pass


pr1 = PowerRobot()
print(pr1.getHp())
