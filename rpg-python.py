class Personagem:
  def __init__(self, nome, vida, forca, elixir, arma):
    self.nome = nome
    self.vida = vida
    self.forca = forca
    self.elixir = elixir
    self.arma = arma

  def ataque_base(self, alvo):
    dano = self.forca
    alvo.vida -= dano
    print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano")

  def ataque_1(self, alvo):
    dano = self.forca + (self.forca // 2)
    alvo.vida -= dano
    self.elixir -= 1
    print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano, restando {self.elixir} de elixir")

  def ataque_2(self, alvo):
    dano = self.forca + self.arma.dano
    alvo.vida -= dano
    self.elixir -= 3
    print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano, restando {self.elixir} de elixir")

class Guerreiro(Personagem):
  def __init__(self, nome):
    super().__init__(nome, vida=150, forca=5, elixir=4, arma=Espada())

  def ataque_especial(self, alvo):
    dano = (self.forca + self.arma.dano) * 2
    alvo.vida -= dano
    self.elixir -= 7
    print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano, restando {self.elixir} de elixir")

class Mago(Personagem):
  def __init__(self, nome):
    super().__init__(nome, vida=100, forca=2, elixir=4, arma=Cajado())

  def ataque_especial(self, alvo):
    dano = (self.forca + self.arma.dano) * 2
    alvo.vida -= dano
    self.elixir -= 7
    print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano, restando {self.elixir} de elixir")

class Arma:
  def __init__(self, nome, dano):
    self.nome = nome
    self.dano = dano

class Espada(Arma):
  def __init__(self, dano=30):
    super().__init__("Espada", dano)

class Cajado(Arma):
  def __init__(self, dano=25):
    super().__init__("Cajado", dano)

jogador1 = Guerreiro("Pedro")
jogador2 = Mago("Carlos")

print(f"Jogador1 vida: {jogador1.vida}")
print(f"Jogador1 força: {jogador1.forca}")
print(f"Dano da {jogador1.arma.nome}: {jogador1.arma.dano}")
print("--------------")
print(f"Jogador2 vida: {jogador2.vida}")
print(f"Jogador2 força: {jogador2.forca}")
print(f"Dano da {jogador2.arma.nome}: {jogador2.arma.dano}")

print("-------TESTE ATAQUE-------")
jogador1.ataque_base(jogador2)
jogador1.ataque_1(jogador2)
jogador1.ataque_2(jogador2)
jogador1.ataque_especial(jogador2)
print("-------TESTE ATAQUE MAGO-------")
jogador2.ataque_base(jogador1)
jogador2.ataque_1(jogador1)
jogador2.ataque_2(jogador1)
jogador2.ataque_especial(jogador1)

print(f"Jogador1 vida: {jogador1.vida}")
print(f"Jogador1 força: {jogador1.forca}")
print(f"Dano da {jogador1.arma.nome}: {jogador1.arma.dano}")
print("--------------")
print(f"Jogador2 vida: {jogador2.vida}")
print(f"Jogador2 força: {jogador2.forca}")
print(f"Dano da {jogador2.arma.nome}: {jogador2.arma.dano}")

