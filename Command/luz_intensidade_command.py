from .command import Command
from .luz import Luz

class Luz_Power_Command(Command):

    def __init__(self, luz:Luz) -> None:
        self.luz = luz

    def execute(self):
        Intensidade = self.luz.aumentarIntensidade()
        print(f'Intensidade da Luz do {self.luz.nome} é {Intensidade}')

    def undo(self):
        Intensidade = self.luz.diminuirIntesidade()
        print(f'Intensidade da Luz do {self.luz.nome} é {Intensidade}')