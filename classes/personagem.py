from classes.arma import Espada, Cajado

class Personagem:
    def __init__(self, nome, vida, vida_max, forca, elixir, arma):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida_max
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
        print(f"{self.nome} recebeu {dano} de dano! (Vida: {self.vida})")

    def ataque_base(self, alvo):
        dano = self.forca
        print(f"{self.nome} socou {alvo.nome}!")
        alvo.receber_dano(dano)
        return True

    def ataque_1(self, alvo):
        custo = 1
        if self.elixir < custo:
            print(f"{self.nome} não tem elixir suficiente!")
            return False
        
        dano = self.forca + (self.forca // 2)
        self.elixir -= custo
        print(f"{self.nome} chutou {alvo.nome}!")
        alvo.receber_dano(dano)
        return True

    def ataque_2(self, alvo):
        custo = 3
        if self.elixir < custo:
            print(f"{self.nome} não tem elixir suficiente!")
            return False
        
        dano = self.forca + self.arma.dano
        self.elixir -= custo
        print(f"{self.nome} atacou {alvo.nome} com sua arma!")
        alvo.receber_dano(dano)
        return True

    def defender(self):
        self.defendendo = True
        print(f"{self.nome} está se defendendo!")
    
    def cura(self):
        custo = 4
        if self.elixir < custo:
            print(f"{self.nome} não tem elixir suficiente!")
            return False
        
        self.vida += 30
        self.elixir -= custo
        if self.vida > self.vida_max:
            self.vida = self.vida_max
        print(f"{self.nome} curou 30 de vida!")   
        return True

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, vida_max = 100, forca=5, elixir=4, arma=Espada())

    def ataque_especial(self, alvo):
            custo = 7
            if self.elixir < custo:
                print(f"{self.nome} não tem elixir suficiente!")
                return False
            
            dano = (self.forca + self.arma.dano) * 2
            self.elixir -= custo
            print(f"{self.nome} utilizou o 🔥 ATAQUE ESPECIAL DO GUERREIRO!") 
            alvo.receber_dano(dano)
            return True

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 150, 150, 2, 4, Cajado())

    def ataque_especial(self, alvo):
          custo = 7
          if self.elixir < custo:
              print(f"{self.nome} não tem elixir suficiente!")
              return False
          
          dano = (self.forca + self.arma.dano) * 2
          self.elixir -= custo
          print(f"{self.nome} lançou a ✨ MAGIA SUPREMA!")
          alvo.receber_dano(dano)
          return True
