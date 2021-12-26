from abstractCar import AbstractCar

class RegularCar(AbstractCar):

    def __init__(self) -> None:
        self.porta = None
        self.qtd_portas = None
        self.pneus = None
        self.parabrisa = None
        self.motor = None
        self.nivel_combustivel = None
        self.tipo_combustivel = None
        self.cambio = None

    def add_porta(self,qtd_porta,tipo_porta):
        self.porta = tipo_porta
        self.qtd_portas = qtd_porta
        print(f'criando {qtd_porta} portas do tipo {tipo_porta}.')

    def add_pneu(self,tipo_pneu):
        self.pneus = tipo_pneu
    
    def add_parabrisa(self,tipo_parabrisa):
        self.parabrisa = tipo_parabrisa

  
    def add_motor(self, tipo_motor):
        self.motor = tipo_motor

   
    def abastecer(self):
        pass

 
    def add_cambio(self):
        pass

