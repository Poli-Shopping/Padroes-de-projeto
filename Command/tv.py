class TV():
    
    def __init__(self, nome) -> None:
        self.nome = nome
        self.is_on = False
        self.brilho = 50
        self.volume = 20
        self.canal_atual = 13

    def ligar(self):
        self.is_on = True
        print(f"A tv foi ligada com sucesso.")
        return self.is_on
    
    def desligar(self):
        self.is_on = False
        print(f"A tv foi desligada com sucesso.")
        return self.is_on

    def aumentar_brilho(self):
        if self.brilho < 100:
            self.brilho += 1
            print(f"O brilho está em {self.brilho}%.")
        else:
            print(f"O brilho já está no máximo.")
        return self.brilho

    def diminuir_brilho(self):
        if self.brilho > 0:
            self.brilho -= 1
            print(f"O brilho está em {self.brilho}%.")
        else:
            print(f"O brilho já está no mínimo.")
        return self.brilho

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"O volume está em {self.volume}.")
        else:
            print(f"O volume já está no máximo.")
        return self.volume

    def diminuir_volume(self):
        if self.volume < 100:
            self.volume -= 1
            print(f"O volume está em {self.volume}.")
        else:
            print(f"O volume já está no máximo.")
        return self.volume

    def mudar_canal(self, canal):
        if self.is_on:
            self.canal_atual = canal
            print(f"Mudança para o canal {self.canal_atual}")
            return self.canal
        else:
            print("A TV está desligada")
            return self.canal_atual


    def status_tv(self):
        msg_ligada = f"A TV {self.nome} está ligada no canal {self.canal_atual} com volume {self.volume} e brilho {50}%."
        return msg_ligada if self.is_on else f"A TV {self.nome} está desligada."
    