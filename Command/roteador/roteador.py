class Roteador():

    def __init__(self) -> None:
        self.is_on = False
        self.velocidade_Download = 200
        self.velocidade_Upload = 100
    
    def status_Rot(self):
        if(self.is_on == True): return "LIGADO"
        else: return "DESLIGADO"

    def ligar(self):
        self.is_on = True
        print("O Roteador está ligado!")
        return self.is_on

    def desligar(self):
        self.is_on = False
        print("O Roteador está desligado!")
        return self.is_on

    def status_Conexao(self):
        print(f"O roteador está com: {self.velocidade_Download}Mb de Download!\n")
        print(f"O roteador está com: {self.velocidade_Upload}Mb de Upload!")
        return self.velocidade_Download
