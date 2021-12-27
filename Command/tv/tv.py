class TV():
    
    def __init__(self, nome) -> None:
        self.nome = nome
        self.is_on = False
        self.brilho = 50
        self.volume = 20
        self.canal_atual = 13
        self.canal_anteiror = None

    def ligar(self):
        self.is_on = True
        return self.is_on
    
    def desligar(self):
        self.is_on = False
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
        if self.is_on:
            if self.volume < 100:
                self.volume += 1
                print(f"O volume está em {self.volume}.")
            else:
                print(f"O volume já está no máximo.")
            return self.volume
        else:
            print("A TV está desligada")
            return self.volume

    def diminuir_volume(self):
        if self.is_on:
            if self.volume > 0:
                self.volume -= 1
                print(f"O volume está em {self.volume}.")
            else:
                print(f"O volume já está no máximo.")
            return self.volume
        else:
            print("A TV está desligada")
            return self.volume

    def mudar_canal(self, canal):
        if self.is_on:
            self.canal_anteiror = self.canal_atual
            self.canal_atual = canal
            print(f"Mudança do canal {self.canal_anteiror} para o canal {self.canal_atual}")
            return self.canal_atual
        else:
            print("A TV está desligada")
            return self.canal_atual

    def voltar_canal(self):
        if self.is_on:
            canal = self.canal_atual
            self.canal_atual = self.canal_anteiror
            self.canal_anteiror = canal
            print(f"Mudança do canal {self.canal_anteiror} para o canal {self.canal_atual}")
            return self.canal_atual
        else:
            print("A TV está desligada")
            return self.canal_atual

    def __str__(self):
        msg_ligada = f"A TV '{self.nome}' está ligada no canal {self.canal_atual} com volume {self.volume} e brilho {self.brilho}%."
        msg_desligada = f"A TV '{self.nome}' está desligada."
        return msg_ligada if self.is_on else msg_desligada
