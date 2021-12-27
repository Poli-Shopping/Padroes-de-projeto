from .command import Command
from .luz import Luz

class LuzPowerCommand(Command):

    def __init__(self, luz:Luz) -> None:
        self.luz = luz

    def execute(self):
        self.luz.ligar()

    def undo(self):
        self.luz.desligar()

    
