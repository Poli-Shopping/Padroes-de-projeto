
from .command import Command
from .luz import Luz

class Luz_Power_Command(Command):

    def __init__(self, luz:Luz) -> None:
        self.luz = luz

    def execute(self,cor):
        self.luz.mudarCor(cor)
    

    