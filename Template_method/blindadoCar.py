from abstractCar import AbstractCar

class BlindadoCar(AbstractCar):

    def __init__(self) -> None:
        super().__init__()
        self.porta = None
        self.qtd_portas = None
        self.pneus = None
        self.parabrisa = None
        self.motor = None
        self.nivel_combustivel = None
        self.tipo_combustivel = None
        self.cambio = None
        self.modo_anfibio = False

    def add_porta(self, qtd_porta):
        self.porta = "Blindada"
        self.qtd_portas = qtd_porta
        print(f'criando {self.qtd_porta} portas do tipo {self.porta}.')

    def add_pneu(self):
        self.pneus = "À prova de balas"
        print(f'criando 4 pneus do tipo {self.pneus}.')
    
    def add_parabrisa(self):
        self.parabrisa = "À prova de balas"
        print(f'criando parabrisa do tipo {self.parabrisa}.')

    def add_motor(self, tipo_motor):
        self.motor = tipo_motor
        print(f'criando motor do tipo {self.motor}.')

    def abastecer(self, ):
        self.nivel_combustivel = 100
        print(f'Combutível tipo {self.nivel_combustivel}.\nNível atual do combutível {self.nivel_combustivel}%.')

    def add_tipo_combustivel(self):
        self.tipo_combustivel = "gasolina"
        print(f"Combustível do tipo {self.tipo_combustivel}.")

    def add_cambio(self):
        self.cambio = "automático"
        print(f"Cambio do tipo {self.cambio}.")

    def ativar_modo_anfibio(self):
        self.modo_anfibio = True
        print(f"Modo anfíbio ativado.")

    def desativar_modo_anfibio(self):
        self.modo_anfibio = False
        print(f"Modo anfíbio desativado.")
