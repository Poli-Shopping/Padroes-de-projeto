from multipledispatch import dispatch
from typing import overload


class CasaInteligenteInvoker():

    def __init__(self) -> None:
        self.commands = {}

    def addCommands(self, key, commands):
        self.commands[key] = commands
    
    @dispatch(str)
    def executar_comando(self,key):
        self.commands[key].execute() if key in self.commands else print('não contém')

    @dispatch(str, str)
    def executar_comando(self, key, param):
        self.commands[key].execute(param) if key in self.commands else print('não contém')

    def undo_comando(self,key):
        self.commands[key].undo() if key in self.commands else print('não contém')
