class Rifle:
    def shot(self):
        print("Rifle")


class Shotgun(Rifle):
    def shot(self):
        print("shotgun")


class SniperRifle(Rifle):
    def shot(self):
        print("sniper")


r = Rifle()
s = Shotgun()
sr = SniperRifle()

r.shot()
s.shot()
sr.shot()
