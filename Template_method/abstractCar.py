from abc import abstractmethod


class AbstractCar():

    def __init__(self) -> None:
        self.porta = None
        self.rodas = None
        self.motor = None
        self.combustivel = None
        self.cambio = None

    @abstractmethod
    def add_porta(self):
        pass

    @abstractmethod
    def add_rodas(self):
        pass

    @abstractmethod
    def add_motor(self):
        pass

    @abstractmethod
    def abastecer(self):
        pass

    @abstractmethod
    def add_cambio(self):
        pass
