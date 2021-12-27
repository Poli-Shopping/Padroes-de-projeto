class CasaInteligenteInvoker():

    def __init__(self) -> None:
        self.commands = {}

    def addCommands(self, key, commands):
        self.commands[key] = commands
    
    def executar_comando(self,key):
        
        if key in self.commands: print('não contém')
        else:
            self.commands[key].execute()

    def undo_comando(self,key):
        
        if key in self.commands: print('não contém')
        else:
            self.commands[key].undo()
