from command import Command
from .arCondicionado import ArCondicionado

class Ar_power_command(Command):

    def __init__(self, arCondicionado: ArCondicionado) -> None:
        self.arCondicionado = arCondicionado

    def execute(self):
        self.arCondicionado.ligar()
        

    def undo(self):
        self.arCondicionado.desligar()