from command import Command
from .arCondicionado import ArCondicionado

class Ar_temperatura_command(Command):

    def __init__(self, arCondicionado: ArCondicionado) -> None:
        self.arCondicionado = arCondicionado

    def execute(self):
        self.arCondicionado.diminuir_temperatura()
        print(f'Temperatura do Ar do(a) {self.arCondicionado.nome} é de {self.arCondicionado.temperatura} graus.')

    def undo(self):
        self.arCondicionado.aumentar_temperatura()
        print(f'Temperatura do Ar do(a) {self.arCondicionado.nome} é de {self.arCondicionado.temperatura} graus')