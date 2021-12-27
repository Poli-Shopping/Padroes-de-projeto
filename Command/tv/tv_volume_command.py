from .command import Command
from .tv import TV

class TVVolumeCommand(Command):

    def __init__(self, tv:TV) -> None:
        self.tv = tv

    def execute(self):
        self.tv.aumentar_volume()

    def undo(self):
        self.tv.diminuir_volume()
