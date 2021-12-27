from casainteligente_invoker import CasaInteligenteInvoker

from luz.luz_power_command import LuzPowerCommand
from luz.luz import  Luz

from tv.tv import TV
from tv.tv_power_command import TVPowerCommand
from tv.tv_brilho_command import TVBrilhoCommand
from tv.tv_volume_command import TVVolumeCommand
from tv.tv_mudar_canal_command import TVMudarCanalCommand
from tv.tv_status_command import TVStatusCommand

from computador.computador import Computador
from computador.computador_power_command import ComputadorPowerCommand


def run_TV(vanellope: CasaInteligenteInvoker):
    TV_quarto = TV('TV do quarto')
    TV_quarto_power_command = TVPowerCommand(TV_quarto)
    TV_quarto_brilho_command = TVBrilhoCommand(TV_quarto)
    TV_quarto_volume_command = TVVolumeCommand(TV_quarto)
    TV_quarto_mudar_canal_command = TVMudarCanalCommand(TV_quarto)
    TV_quarto_status_command = TVStatusCommand(TV_quarto)

    TV_sala = TV('TV da sala')
    TV_sala_power_command = TVPowerCommand(TV_sala)
    TV_sala_brilho_command = TVBrilhoCommand(TV_sala)
    TV_sala_volume_command = TVVolumeCommand(TV_sala)
    TV_sala_mudar_canal_command = TVMudarCanalCommand(TV_sala)
    TV_sala_status_command = TVStatusCommand(TV_sala)


    vanellope.addCommands('tv quarto power', TV_quarto_power_command)
    vanellope.addCommands('tv quarto brilho', TV_quarto_brilho_command)
    vanellope.addCommands('tv quarto volume', TV_quarto_volume_command)
    vanellope.addCommands('tv quarto mudar canal', TV_quarto_mudar_canal_command)
    vanellope.addCommands('tv quarto status', TV_quarto_status_command)

    vanellope.addCommands('tv sala power', TV_sala_power_command)
    vanellope.addCommands('tv sala brilho', TV_sala_brilho_command)
    vanellope.addCommands('tv sala volume', TV_sala_volume_command)
    vanellope.addCommands('tv sala mudar canal', TV_sala_mudar_canal_command)
    vanellope.addCommands('tv sala status', TV_sala_status_command)

    vanellope.executar_comando('tv quarto power')
    [vanellope.executar_comando('tv quarto brilho') for _ in range(51)]
    [vanellope.undo_comando('tv quarto volume') for _ in range(21)]
    vanellope.executar_comando('tv sala mudar canal', '9')
    
    vanellope.executar_comando('tv sala power')
    [vanellope.undo_comando('tv sala brilho') for _ in range(51)]
    [vanellope.executar_comando('tv sala volume') for _ in range(81)]
    vanellope.executar_comando('tv sala mudar canal', '2')
    
    vanellope.executar_comando('tv quarto status')
    vanellope.executar_comando('tv sala status')

    vanellope.undo_comando('tv quarto power')
    vanellope.undo_comando('tv sala power')

def run_computador(vanellope: CasaInteligenteInvoker):
    computador = Computador('Jarvis')
    jarvis_power_command = ComputadorPowerCommand(computador)
    
    vanellope.addCommands('acorda criança, o papai chegou!', jarvis_power_command)
    
    vanellope.executar_comando('acorda criança, o papai chegou!')
    vanellope.undo_comando('acorda criança, o papai chegou!')

def run():
    vanellope = CasaInteligenteInvoker()
    #run_TV(vanellope)
    run_computador(vanellope)

run()
