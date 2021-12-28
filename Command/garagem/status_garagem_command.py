from command import Command
from .garagem import Garagem

class GaragemStatus(Command):

    def __init__(self, garagem:Garagem) -> None:
        self.garagem = garagem

    def execute(self):
        print(self.garagem.verificarStatus())
        
    def undo(self):
        print("Essa classe não possui um método undo.")
