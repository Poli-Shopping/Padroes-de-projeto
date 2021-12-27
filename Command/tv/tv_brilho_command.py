from .command import Command
from .tv import TV

class TVBrilhoCommand(Command):

    def __init__(self, tv:TV) -> None:
        self.tv = tv

    def execute(self):
        self.tv.aumentar_brilho()

    def undo(self):
        self.tv.diminuir_brilho()
