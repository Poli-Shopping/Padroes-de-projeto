from casainteligente_invoker import CasaInteligenteInvoker

from luz.luz_power_command import LuzPowerCommand
from luz.luz_intensidade_command import LuzIntensidadeCommand
from luz.luz_cor_command import LuzCorCommand
from luz.luz import  Luz

from tv.tv import TV
from tv.tv_power_command import TVPowerCommand
from tv.tv_brilho_command import TVBrilhoCommand
from tv.tv_volume_command import TVVolumeCommand
from tv.tv_mudar_canal_command import TVMudarCanalCommand
from tv.tv_status_command import TVStatusCommand

from roteador.roteador import Roteador
from roteador.roteador_power_command import Roteador_power_command
from roteador.roteador_velocidade_command import Roteador_velocidade_command

from arcondicionado.arCondicionado import ArCondicionado
from arcondicionado.ar_temperatura_command import Ar_temperatura_command
from arcondicionado.ar_power_command import Ar_power_command

from computador.computador import Computador
from computador.computador_power_command import ComputadorPowerCommand

from garagem.garagem import Garagem
from garagem.garagem_open_command import GaragemOpen
from garagem.status_garagem_command import GaragemStatus

def run_light(vanellope: CasaInteligenteInvoker):
    luz_quarto = Luz('quarto')
    luz_quarto_power_command = LuzPowerCommand(luz_quarto)
    luz_quarto_intensidade_command = LuzIntensidadeCommand(luz_quarto)
    luz_quarto_cor_command = LuzCorCommand(luz_quarto)

    luz_sala = Luz('sala')
    luz_sala_power_command = LuzPowerCommand(luz_sala)
    luz_sala_intensidade_command = LuzIntensidadeCommand(luz_sala)
    luz_sala_cor_command = LuzCorCommand(luz_sala)

    vanellope.addCommands('luz quarto power',  luz_quarto_power_command)
    vanellope.addCommands('luz quarto intensidade', luz_quarto_intensidade_command)
    vanellope.addCommands('luz quarto mudar cor', luz_quarto_cor_command)

    vanellope.addCommands('luz sala power',  luz_sala_power_command)
    vanellope.addCommands('luz sala intensidade', luz_sala_intensidade_command)
    vanellope.addCommands('luz sala mudar cor', luz_sala_cor_command)

    vanellope.executar_comando('luz sala power')
    [vanellope.executar_comando('luz sala intensidade') for _ in range(51)]
    vanellope.executar_comando('luz sala mudar cor','azul')
    [vanellope.undo_comando('luz sala intensidade') for _ in range(20)]
    vanellope.undo_comando('luz sala power')

    vanellope.executar_comando('luz quarto power')
    [vanellope.undo_comando('luz quarto intensidade') for _ in range(51)]
    [vanellope.executar_comando('luz quarto intensidade') for _ in range(20)]
    vanellope.executar_comando('luz quarto mudar cor','roxo')
    vanellope.undo_comando('luz quarto power')

def run_garagem(vanellope: CasaInteligenteInvoker):
    garagem = Garagem()
    garagem_open_command = GaragemOpen(garagem)
    garagem_status_command = GaragemStatus(garagem)

    vanellope.addCommands('garagem open',  garagem_open_command)
    vanellope.addCommands('verificarGaragem', garagem_status_command)

    vanellope.executar_comando('garagem open')
    vanellope.executar_comando('verificarGaragem')
    vanellope.undo_comando('garagem open')

def run_arCondicionado(vanellope: CasaInteligenteInvoker):
    Ar_quarto = ArCondicionado("Quarto")
    Ar_quarto_power_command = Ar_power_command(Ar_quarto)
    Ar_quarto_temperatura_command = Ar_temperatura_command(Ar_quarto)

    Ar_sala = ArCondicionado("Sala")
    Ar_sala_power_command = Ar_power_command(Ar_sala)
    Ar_sala_temperatura_command = Ar_temperatura_command(Ar_sala)

    vanellope.addCommands('Ar quarto power',  Ar_quarto_power_command)
    vanellope.addCommands('Ar quarto temperatura',  Ar_quarto_temperatura_command)

    vanellope.addCommands('Ar sala power',  Ar_sala_power_command)
    vanellope.addCommands('Ar sala temperatura',  Ar_sala_temperatura_command)

    vanellope.executar_comando('Ar quarto power')
    [vanellope.executar_comando('Ar quarto temperatura') for _ in range(5)]
    vanellope.undo_comando('Ar quarto power')
    [vanellope.undo_comando('Ar quarto temperatura')for _ in range(6)]

    vanellope.executar_comando('Ar sala power')
    [vanellope.executar_comando('Ar sala temperatura')for _ in range(10)]
    vanellope.undo_comando('Ar sala power')
    [vanellope.undo_comando('Ar sala temperatura')for _ in range(6)]

def run_roteador(vanellope: CasaInteligenteInvoker):
    roteador = Roteador()
    roteador_power_command = Roteador_power_command(roteador)
    roteador_velocidade_command = Roteador_velocidade_command(roteador)

    vanellope.addCommands('Roteador ligar!',  roteador_power_command)
    vanellope.addCommands('Roteador mostrar velocidade',  roteador_velocidade_command)

    vanellope.executar_comando('Roteador ligar!')
    vanellope.executar_comando('Roteador mostrar velocidade')
    vanellope.undo_comando('Roteador ligar!')


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
    print("EXEMPLO TV")
    run_TV(vanellope)
    print("EXEMPLO PC")
    run_computador(vanellope)
    print("EXEMPLO LUZ")
    run_light(vanellope)
    print("EXEMPLO GARAGEM")
    run_garagem(vanellope)
    print("EXEMPLO AR CONDICIONADO")
    run_arCondicionado(vanellope)
    print("EXEMPLO ROTEADOR")
    run_roteador(vanellope)
run()
