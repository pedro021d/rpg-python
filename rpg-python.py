import os
import random

from classes.personagem import Guerreiro, Mago

os.system("cls" if os.name == "nt" else "clear")
print("═" * 52)
print("  ⚔️   ARENA OF THRONES - CONSOLE EDITION   ⚔️")
print("═" * 52)
print("""
  Bem-vindo à arena!
  Escolha seu herói, enfrente o inimigo
  e tente sair vivo desta batalha épica.
""")

def mostrar_interface():
    print("\n" + "=" * 40)
    print(f"{jogador.nome}: {jogador.vida} | Elixir: {jogador.elixir}")
    print(f"Inimigo: {inimigo.vida}")
    print("=" * 40)

    print("\nEscolha sua ação:")
    print("1 - Ataque Básico (0 elixir)")
    print("2 - Ataque 1 (1 elixir)")
    print("3 - Ataque 2 (3 elixir)")
    print("4 - Ataque Especial (7 elixir)")
    print("5 - Defender")
    print("6 - Curar")

# Escolha do nome
print("=== DEFINA O NOME DO SEU PERSONAGEM ===")
nome = input("Nome: ")

# Escolha da classe
print("=== ESCOLHA SUA CLASSE ===")
print("1 - Guerreiro")
print("2 - Mago")

classe = input("Escolha: ")
if classe == "1":
    jogador = Guerreiro(nome)
    inimigo = Mago("Mago")
else:
    jogador = Mago(nome)
    inimigo = Guerreiro("Guerreiro")

# Loop da batalha
while jogador.vida > 0 and inimigo.vida > 0:
    mostrar_interface()

    while True:
        escolha = input("Ação: ")

        if escolha == "1":
            jogador.ataque_base(inimigo)
            break

        elif escolha == "2":
            if jogador.ataque_1(inimigo) is False:
                continue
            break

        elif escolha == "3":
            if jogador.ataque_2(inimigo) is False:
                continue
            break

        elif escolha == "4":
            if jogador.ataque_especial(inimigo) is False:
                continue
            break

        elif escolha == "5":
            jogador.defender()
            break

        elif escolha == "6":
            if jogador.cura() is False:
                continue
            break
                
        else:
            print("Opção inválida!")
            continue

    # Turno do inimigo
    if inimigo.vida > 0:
        if inimigo.vida < 30 and inimigo.elixir >= 4:
            inimigo.cura()
        else:
            dano_inimigo = random.randint(8, 15)
            jogador.receber_dano(dano_inimigo)

# Resultado
print("\n===== FIM DA BATALHA =====")
if jogador.vida > 0:
    print("Você venceu!")
else:
    print("Você perdeu!")
