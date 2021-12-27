class Computador():

    def __init__(self, nome) -> None:
        self.is_on = False
    
    def acorda_crianca_o_papai_chegou(self):
        self.is_on = True
        print("Bem vindo, senhor! \nParabéns Pela cerimônia de abertura, foi um sucesso!")
        return self.is_on
    
    def desligar(self):
        self.is_on = False
        print("O computador foi desligado com sucesso.")
        return self.is_on

    def status_computador(self):
        msg_ligado = f"O computador {self.nome} está ligado"
        msg_desligado = f"O computador {self.nome} está desligado."
        return msg_ligado if self.is_on else msg_desligado
