from Template_method.blindadoCar import BlindadoCar
from Template_method.regularCar import RegularCar
from Template_method.electricCar import ElectricCar


def run_carro_blindado():
    carro_blindado = BlindadoCar(4, "V8")

    carro_blindado.andar(250)
    carro_blindado.ativar_modo_anfibio()
    carro_blindado.andar(250)
    carro_blindado.desativar_modo_anfibio()
    carro_blindado.andar(350)
    carro_blindado.andar(250)
    carro_blindado.abastecer()
    carro_blindado.andar(250)

    
def run_carro_eletrico():
    carro_eletrico = ElectricCar()


def run_carro_regular():
    carro_regular = RegularCar()


def run():
    run_carro_regular()
    run_carro_blindado()
    run_carro_eletrico()


run()