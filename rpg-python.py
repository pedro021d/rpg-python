import os

from classes.personagem import Guerreiro, Mago
from classes.partida import Partida

os.system("cls" if os.name == "nt" else "clear")
print("═" * 52)
print("  ⚔️   ARENA OF THRONES - CONSOLE EDITION   ⚔️")
print("═" * 52)
print("""
  Bem-vindo à arena!
  Escolha seu herói, enfrente o inimigo
  e tente sair vivo desta batalha épica.
""")

# Escolha do nome
print("=== DEFINA O NOME DO SEU PERSONAGEM ===")
nome = input("Nome: ").capitalize()   

# Escolha da classe
print("\n=== ESCOLHA SUA CLASSE ===")
print("1 - Guerreiro")
print("2 - Mago")
classe = input("Escolha: ")

if classe == "1":
    jogador = Guerreiro(nome)
    inimigo = Mago("Mago")
else:
    jogador = Mago(nome)
    inimigo = Guerreiro("Guerreiro")

# Inicia partida
partida = Partida(jogador, inimigo)
partida.iniciar()