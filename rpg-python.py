import os, random
from classes.personagem import Guerreiro, Mago

jogador1 = Guerreiro("Pedro")
jogador2 = Mago("Carlos")

print(f"Jogador1 vida: {jogador1.vida}")
print(f"Jogador1 força: {jogador1.forca}")
print(f"Dano da {jogador1.arma.nome}: {jogador1.arma.dano}")
print("--------------")
print(f"Jogador2 vida: {jogador2.vida}")
print(f"Jogador2 força: {jogador2.forca}")
print(f"Dano da {jogador2.arma.nome}: {jogador2.arma.dano}")

os.system("cls" if os.name == "nt" else "clear")
print("═" * 52)
print("  ⚔️   RPG DE BATALHA — CONSOLE EDITION   ⚔️")
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
input("Nome: ")


# Escolha da classe
print("=== ESCOLHA SUA CLASSE ===")
print("1 - Guerreiro")
print("2 - Mago")

classe = input("Escolha: ")
if classe == "1":
    jogador = Guerreiro("Guerreiro")
    inimigo = Mago("Mago")
else:
    jogador = Mago("Mago")
    inimigo = Guerreiro("Guerreiro")

# Loop da batalha
while jogador.vida > 0 and inimigo.vida > 0:
    mostrar_interface()
    escolha = input("Ação: ")

    dano = 0

    if escolha == "1":
        jogador.ataque_base(inimigo)

    elif escolha == "2":
        if jogador.elixir >= 1:
            jogador.elixir -= 1
            jogador.ataque_1(inimigo)
        else:
            print("Elixir insuficiente!")
            continue

    elif escolha == "3":
        if jogador.elixir >= 3:
            jogador.elixir -= 3
            jogador.ataque_2(inimigo)
        else:
            print("Elixir insuficiente!")
            continue

    elif escolha == "4":
        if jogador.elixir >= 7:
            jogador.elixir -= 7
            jogador.ataque_especial(inimigo)
        else:
            print("Elixir insuficiente!")
            continue

    elif escolha == "5":
        jogador.defendendo = True
        print("Você está defendendo!")

    elif escolha == "6":
        jogador.cura()
            
    else:
        print("Opção inválida!")
        continue

    if dano > 0:
        print(f"Você causou {dano} de dano!")
        inimigo.receber_dano(dano)

    # Turno do inimigo
    if inimigo.vida > 0:
        dano_inimigo = random.randint(8, 15)
        print(f"Inimigo atacou causando {dano_inimigo} de dano!")
        jogador.receber_dano(dano_inimigo)

# Resultado
print("\n===== FIM DA BATALHA =====")
if jogador.vida > 0:
    print("Você venceu!")
else:
    print("Você perdeu!")


