# override


class Phone:
    def call(self):
        print("calling...")


class SmartPhone(Phone):
    def __init__(self) -> None:
        super().__init__()

    def call(self):
        print("SmartCalling...")


s1 = SmartPhone()
s1.call()
