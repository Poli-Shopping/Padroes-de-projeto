from luz.luz_power_command import LuzPowerCommand
from luz.luz import  Luz
from .CasaInteligente_invoker import CasaInteligenteInvoker

luz_quarto = Luz('Quarto')
luz_power = LuzPowerCommand(Luz)
luz_quarto.is_on()
