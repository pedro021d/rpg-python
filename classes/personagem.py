from classes.arma import Espada, Cajado

class Personagem:
    def __init__(self, nome, vida, forca, elixir, arma):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.elixir = elixir
        self.arma = arma
        self.defendendo = False

    def receber_dano(self, dano):
        if self.defendendo:
            dano = dano // 2
            self.defendendo = False

        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {dano} de dano (Vida: {self.vida})")

    def tem_elixir(self, custo):
        return self.elixir >= custo

    def ataque_base(self, alvo):
        dano = self.forca
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano")

    def ataque_1(self, alvo):
        custo = 1
        if not self.tem_elixir(custo):
            print(f"{self.nome} não tem elixir suficiente!")
            return
        
        dano = self.forca + (self.forca // 2)
        alvo.receber_dano(dano)
        self.elixir -= custo
        print(f"{self.nome} causou {dano} de dano (Elixir: {self.elixir})")

    def ataque_2(self, alvo):
        custo = 3
        if not self.tem_elixir(custo):
            print(f"{self.nome} não tem elixir suficiente!")
            return
        
        dano = self.forca + self.arma.dano
        alvo.receber_dano(dano)
        self.elixir -= custo
        print(f"{self.nome} causou {dano} de dano (Elixir: {self.elixir})")

    def defender(self):
        self.defendendo = True
        print(f"{self.nome} se defendeu!")
    
    def cura(self):
        custo = 4
        if not self.tem_elixir(custo):
            print(f"{self.nome} não tem elixir suficiente!")
            return False
        
        self.vida += 30
        self.elixir -= custo
        print(f"{self.nome} recuperou 30 de vida (Vida: {self.vida})")   

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, forca=5, elixir=4, arma=Espada())

    def ataque_especial(self, alvo):
            custo = 7
            if not self.tem_elixir(custo):
                print(f"{self.nome} não tem elixir suficiente!")
                return
            
            dano = (self.forca + self.arma.dano) * 2
            alvo.receber_dano(dano)
            self.elixir -= custo
            print(f"{self.nome} causou {dano} de dano (ESPECIAL) (Elixir: {self.elixir})")

    def cura(self):
        custo = 4
        if not self.tem_elixir(custo):
            print(f"{self.nome} não tem elixir suficiente!")
            return False
        
        if self.vida >= 100:
            print(f"{self.nome} já está com a vida cheia!")
            return False
        
        if self.vida >= 70:
            self.vida += 30
            self.elixir -= custo
            if self.vida > 100:
                self.vida = 100
                return print(f"{self.nome} recuperou 30 de vida (Vida: {self.vida})") 
            return print(f"{self.nome} recuperou 30 de vida (Vida: {self.vida})")  

        self.vida += 30
        self.elixir -= custo

        print(f"{self.nome} recuperou 30 de vida (Vida: {self.vida})")   

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 150, 2, 4, Cajado())
    def ataque_especial(self, alvo):
          custo = 7
          if not self.tem_elixir(custo):
              print(f"{self.nome} não tem elixir suficiente!")
              return
          
          dano = (self.forca + self.arma.dano) * 2
          alvo.receber_dano(dano)
          self.elixir -= custo
          print(f"{self.nome} causou {dano} de dano (ESPECIAL) (Elixir: {self.elixir})")
