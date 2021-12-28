
from command import Command
from .garagem import Garagem

class GaragemOpen(Command):

    def __init__(self, garagem:Garagem) -> None:
        self.garagem = garagem

    def execute(self):
        self.garagem.abrir()
        
    def undo(self):
        self.garagem.fechar()