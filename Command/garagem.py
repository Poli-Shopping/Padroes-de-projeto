from .luz import Luz

class Garagem():

    def __init__(self) -> None:
        self.open = False
        self.luz = Luz('Garagem')

    def abrir(self):
        self.open = True
        self.luz.ligar()
        print('Garagem Abriu')

    def fechar(self):
        self.open = False
        self.luz.desligar()
        print('Garagem fechou')
    
    def verificarStatus(self):
        if self.open : return 'Garagem está aberta'
        else: return 'Garagem está fechada'