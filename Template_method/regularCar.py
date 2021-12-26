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
        print(f'criando {self.qtd_portas} portas do tipo {self.porta}.')

    def add_pneu(self,tipo_pneu):
        self.pneus = tipo_pneu
        print(f'adicionado pneu do tipo {self.pneus}')

    def add_parabrisa(self,tipo_parabrisa):
        self.parabrisa = tipo_parabrisa
        print(f'adicionado parabrisa do tipo {self.parabrisa}')
  
    def add_motor(self, tipo_motor):
        self.motor = tipo_motor
        print(f'adicionado motor do tipo {self.motor}')
   
    def abastecer(self):
        self.nivel_combustivel = 100
        print(f'Nível atual do combutível {self.nivel_combustivel}%.')

    def add_tipo_combustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel
        print(f"Combustível do tipo {self.tipo_combustivel}")

    def add_cambio(self,tipo_cambio):
        self.cambio = tipo_cambio
        print(f'adicionado cambio tipo {tipo_cambio}')

