from command import Command
from .computador import Computador

class ComputadorPowerCommand(Command):

    def __init__(self, computador:Computador) -> None:
        self.computador = computador

    def execute(self):
        self.computador.acorda_crianca_o_papai_chegou()

    def undo(self):
        self.computador.desligar()
        print(self.computador)
