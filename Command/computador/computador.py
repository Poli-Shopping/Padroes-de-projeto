class Computador():

    def __init__(self, nome) -> None:
        self.is_on = False
        self.nome = nome
    
    def acorda_crianca_o_papai_chegou(self):
        self.is_on = True
        print("Bem vindo, senhor! \nParabéns pela cerimônia de abertura, foi um sucesso!")
        return self.is_on
    
    def desligar(self):
        self.is_on = False
        return self.is_on

    def __str__(self):
        msg_ligado = f"O computador '{self.nome}' está ligado"
        msg_desligado = f"O computador '{self.nome}' está desligado."
        return msg_ligado if self.is_on else msg_desligado
