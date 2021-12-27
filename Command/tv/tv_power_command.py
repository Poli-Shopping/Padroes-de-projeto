from .command import Command
from .tv import TV

class TVPowerCommand(Command):

    def __init__(self, tv:TV) -> None:
        self.tv = tv

    def execute(self):
        self.tv.ligar()
        print(self.tv)

    def undo(self):
        self.tv.desligar()
        print(self.tv)
