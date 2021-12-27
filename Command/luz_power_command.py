from .command import Command
from .luz import Luz

class Luz_Power_Command(Command):

    def __init__(self) -> None:
        pass

    def execute():
        Luz.ligar()

    def undo():
        Luz.desligar()

    
