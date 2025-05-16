import requests

class RoboZica:
    def __init__(self, nome="ZikaBuster3000"):
        self.nome = nome
        self.localizacao = (0, 0)

    def receber_localizacao(self, local=None):
        if local:
            print(f"[{self.nome}] Localização recebida: {local}")
            self.ir_para_local(local)
        else:
            print(f"[{self.nome}] Nenhuma localização recebida. Ativando modo 'pernilongo radar'...")
            self.cacar_foco()

    def ir_para_local(self, destino):
        print(f"[{self.nome}] Indo para o local {destino}...")
        time.sleep(1)
        self.localizacao = destino
        print(f"[{self.nome}] Cheguei no local! Preparando fumaça genética...")
        self.soltar_fumaca()

    def cacar_foco(self):
        foco_aleatorio = (random.randint(-100, 100), random.randint(-100, 100))
        print(f"[{self.nome}] Foco suspeito detectado em {foco_aleatorio}. Indo verificar...")
        self.ir_para_local(foco_aleatorio)

    def soltar_fumaca(self):
        efeitos = [
            "Mosquitos confusos começam a estudar filosofia.",
            "Mosquitos agora não conseguem paquerar uns aos outros.",
            "Mosquitos só"
        ]