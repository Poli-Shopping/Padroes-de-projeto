from command import Command
from .roteador import Roteador

class Roteador_velocidade_command(Command):

    def __init__(self, roteador: Roteador) -> None:
        self.roteador = roteador

    def execute(self):
        self.roteador.status_Conexao()
        

    def undo(self):
        print("Essa classe não possui um método undo.")