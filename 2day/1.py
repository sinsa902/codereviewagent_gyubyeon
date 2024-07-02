class Zrgling:
    def __init__(self) -> None:
        self.hp = 20

    def attack(this):
        this.hp += 1
        this.mana -= 10

    def move(this):
        this.hp = 10
        this.hp -= 10
        this.mana += 5

    def status(this):
        print(f"{this.hp},{this.mana}")


z1 = Zrgling()
z2 = Zrgling()

z1.move()
z2.move()
z1.status()
z2.status()
