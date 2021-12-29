from command import Command
from .roteador import Roteador

class Roteador_power_command(Command):

    def __init__(self, roteador: Roteador) -> None:
        self.roteador = roteador

    def execute(self):
        self.roteador.ligar()
        

    def undo(self):
        self.roteador.desligar()