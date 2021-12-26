from .abstractCar import AbstractCar

class RegularCar(AbstractCar):

    def __init__(self, qtd_portas,tipo_porta, tipo_pneu, tipo_combustivel, tipo_motor, tipo_parabrisa, tipo_cambio) -> None:
        super().__init__()
        self.add_porta(qtd_portas,tipo_porta)
        self.add_pneu(tipo_pneu)
        self.add_parabrisa(tipo_parabrisa)
        self.add_motor(tipo_motor)
        self.add_cambio(tipo_cambio)
        self.add_tipo_combustivel(tipo_combustivel)
        self.abastecer()
        print("Carro Regular criado com sucesso!\n\n")

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

    def andar(self, distancia):
        # O carro regular faz 20 km a cada 1% de combustível.
        gasto = distancia / 20
        if self.nivel_combustivel > gasto:
            self.nivel_combustivel -= gasto
            print(f'Combutível tipo {self.tipo_combustivel}.\nNível atual do combutível {self.nivel_combustivel}%.')
        else:
            print(f"Essa distância é maior que o suportado pelo nível de combutível atual")
