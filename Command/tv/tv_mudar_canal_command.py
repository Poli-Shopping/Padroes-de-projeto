from .command import Command
from .tv import TV

class TVMudarCanalCommand(Command):

    def __init__(self, tv:TV) -> None:
        self.tv = tv

    def execute(self, canal):
        self.tv.mudar_canal(canal)

    def undo(self):
        self.tv.voltar_canal()
