import random

class Partida:
    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo

    def mostrar_interface(self):
        print("\n" + "=" * 40)
        print(f"{self.jogador.nome}: {self.jogador.vida} | Elixir: {self.jogador.elixir}")
        print(f"Inimigo: {self.inimigo.vida}")
        print("=" * 40)

        print("\nEscolha sua ação:")
        print(f"[1] Ataque Básico - {self.jogador.forca} dano")
        print(f"[2] Ataque 1 - {self.jogador.forca + (self.jogador.forca // 2)} dano (1 elixir)")
        print(f"[3] Ataque 2 - {self.jogador.forca + self.jogador.arma.dano} dano (3 elixir)")
        print(f"[4] Ataque Especial (7 elixir)")
        print("[5] Defender - reduz o dano pela metade")
        print("[6] Curar - restaura 30 HP(4 elixir)")

    def turno_jogador(self):
        while True:
            escolha = input("Ação: ")

            if escolha == "1":
                self.jogador.ataque_base(self.inimigo)
                break

            elif escolha == "2":
                if self.jogador.ataque_1(self.inimigo) is False:
                    continue
                break

            elif escolha == "3":
                if self.jogador.ataque_2(self.inimigo) is False:
                    continue
                break

            elif escolha == "4":
                if self.jogador.ataque_especial(self.inimigo) is False:
                    continue
                break

            elif escolha == "5":
                self.jogador.defender()
                break

            elif escolha == "6":
                if self.jogador.cura() is False:
                    continue
                break

            else:
                print("Opção inválida!")

    def turno_inimigo(self):
        if self.inimigo.vida <= 0:
            return

        if self.inimigo.vida < 30 and self.inimigo.elixir >= 4:
            self.inimigo.cura()
        else:
            dano = random.randint(8, 15)
            self.jogador.receber_dano(dano)

    def iniciar(self):
        while self.jogador.vida > 0 and self.inimigo.vida > 0:
            self.mostrar_interface()
            self.turno_jogador()
            self.turno_inimigo()
            self.jogador.elixir += 2
            self.inimigo.elixir += 2

        print("\n===== FIM DA BATALHA =====")
        if self.jogador.vida > 0:
            print("Você venceu!")
        else:
            print("Você perdeu!")