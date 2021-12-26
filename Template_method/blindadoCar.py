from .abstractCar import AbstractCar

class BlindadoCar(AbstractCar):

    def __init__(self, qtd_portas, tipo_motor) -> None:
        super().__init__()
        self.add_porta(qtd_portas)
        self.add_pneus()
        self.add_parabrisa()
        self.add_motor(tipo_motor)
        self.add_cambio()
        self.add_tipo_combustivel()
        self.abastecer()
        self.modo_anfibio = False
        print("Carro blindado criado com sucesso!\n\n")

    def add_porta(self, qtd_porta):
        self.porta = "Blindada"
        self.qtd_portas = qtd_porta
        print(f'criando {self.qtd_portas} portas do tipo {self.porta}.')

    def add_pneus(self):
        self.pneus = "Misto - À prova de balas"
        print(f'criando 4 pneus do tipo {self.pneus}.')
    
    def add_parabrisa(self):
        self.parabrisa = "Vidro Temperado"
        print(f'criando parabrisa do tipo {self.parabrisa}.')

    def add_motor(self, tipo_motor):
        self.motor = tipo_motor
        print(f'criando motor do tipo {self.motor}.')

    def abastecer(self):
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

    def andar(self, distancia):
        # O carro blindado faz 10 km a cada 1% de combustível.
        gasto = distancia / 10
        if self.nivel_combustivel > gasto:
            self.nivel_combustivel -= gasto
            print(f'Combutível tipo {self.tipo_combustivel}.\nNível atual do combutível {self.nivel_combustivel}%.')
        else:
            print(f"Essa distância é maior que o suportado pelo nível de combutível atual")
        
