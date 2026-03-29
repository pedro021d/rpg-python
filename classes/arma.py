class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

class Espada(Arma):
    def __init__(self):
        super().__init__("Espada", 30)

class Cajado(Arma):
    def __init__(self):
        super().__init__("Cajado", 20)