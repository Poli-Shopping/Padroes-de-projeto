
class Luz():

    def __init__(self, nome) -> None:
        self.nome = nome
        self.is_on = False
        self.intensidade = 50
        self.cor = 'branca'

    def status_luz(self):
        if self.is_on: return'LIGADA'
        else: return'DESLIGADA'

    def ligar(self):
        self.is_on = True
        return self.is_on

    def desligar(self):
        self.is_on = False
        return self.is_on
    
    def aumentarIntensidade(self):
        if self.intensidade>=100:
            return self.intensidade
        else: 
            self.intensidade += 1
            return self.intensidade

    def diminuirIntesidade(self):
        if self.intensidade<=0:
            return self.intensidade
        else:
            self.intensidade -= 1
            return self.intensidade

    def mudarCor(self,cor):
        self.cor = cor
        return self.cor
    
    
