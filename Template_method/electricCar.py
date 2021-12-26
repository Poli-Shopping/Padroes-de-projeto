from .abstractCar import AbstractCar

class ElectricCar(AbstractCar):

    def __init__(self, qtd_portas, tipo_porta, tipo_pneu,  tipo_parabrisa) -> None:
        super().__init__()
        self.add_porta(qtd_portas, tipo_porta)
        self.add_pneu(tipo_pneu)
        self.add_parabrisa(tipo_parabrisa)
        self.add_motor()
        self.add_cambio()
        self.add_tipo_combustivel()
        self.abastecer()
        print("Carro Regular criado com sucesso!\n\n")
       

    def add_porta(self,qtd_porta,tipo_porta):
        self.porta = tipo_porta
        self.qtd_portas = qtd_porta
        print(f'criando {qtd_porta} portas do tipo {tipo_porta}.')

    def add_pneu(self,tipo_pneu):
        self.pneus = tipo_pneu
        print(f'Criando 4 Pneus do tipo {self.pneu}.')
    
    def add_parabrisa(self,tipo_parabrisa):
        self.parabrisa = tipo_parabrisa
        print(f'Criando parabrisa do tipo {self.parabrisa}.')
  
    def add_motor(self):
        self.motor = "Eletrico"
        print(f'Criando motor do tipo elétrico.')

    def recarregar_bateria(self):
        print(f'Nível atual da bateria {self.nivel_combustivel}%.')
        self.abastecer()
        print(f'Nível atual da bateria {self.nivel_combustivel}%.')
   
    def abastecer(self):
        self.nivel_combustivel = 100
 
    def add_cambio(self):
        self.cambio = "Automátio"
        print(f'Criando câmbio do tipo {self.cambio}.')
