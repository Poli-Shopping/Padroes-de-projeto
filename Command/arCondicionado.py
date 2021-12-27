class ArCondicionado():

    def __init__(self, nome) -> None:
        self.nome = nome
        self.is_on = False
        self.temperatura = 25
    
    def status_Ar(self):
        if(self.is_on == True): return "LIGADO"
        else: return "DESLIGADO"

    def ligar(self):
        self.is_on = True
        print("O Ar-condicionado está ligado!")
        return self.is_on

    def desligar(self):
        self.is_on = False
        print("O Ar-condicionado está desligado!")
        return self.is_on

    def aumentar_temperatura(self):
        if(self.temperatura < 29):
            self.temperatura += 1
        print(f"A temperatura está em: {self.temperatura} graus!")
        return self.temperatura

    def diminuir_temperatura(self):
        if(self.temperatura > 15):
            self.temperatura -= 1
        
        print(f"A temperatura está em: {self.temperatura} graus!")
        return self.temperatura
