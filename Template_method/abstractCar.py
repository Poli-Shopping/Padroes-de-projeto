from abc import abstractmethod


class AbstractCar():

    def __init__(self) -> None:
        self.porta = None
        self.qtd_portas = None
        self.pneus = None
        self.parabrisa = None
        self.motor = None
        self.nivel_combustivel = None
        self.tipo_combustivel = None
        self.cambio = None

    @abstractmethod
    def add_porta(self):
        pass

    @abstractmethod
    def add_pneu(self):
        pass

    @abstractmethod
    def add_parabrisa(self):
        pass

    @abstractmethod
    def add_motor(self):
        pass

    @abstractmethod
    def add_tipo_combustivel(self):
        pass

    @abstractmethod
    def abastecer(self):
        pass

    @abstractmethod
    def add_cambio(self):
        pass
