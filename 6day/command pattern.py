class TV:
    pass


class RemoteControl:
    def __init__(self):
        self.command = None

    def set_cmd(self, command: Command):
        self.command = command

    def run(self):
        self.command.run()


class Command:
    def run(self):
        pass


tv = TV()
com1 = command()
remote = RemoteControl(tv)
remote.set_cmd(com1)
remote.run()
