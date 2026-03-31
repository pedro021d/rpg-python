import random, os

class Partida:
    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo
 
    def limpar(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def barra_vida(self, valor, maximo, tamanho=20):
        proporcao = max(0, min(valor / maximo, 1))
        cheio = int(proporcao * tamanho)
        vazio = tamanho - cheio
        if proporcao > 0.5: cor = "🟩" 
        elif proporcao > 0.25: cor = "🟨" 
        else: cor = "🟥"
        barra_visual = cor * cheio + "⬛" * vazio
        
        return f"[{barra_visual}] {valor}/{maximo}"
    
    def barra(self, valor, maximo, tamanho=10):
        preenchido = int(tamanho * valor // maximo)
        return "[" + "🔵" * preenchido + "-" * (tamanho - preenchido) + "]"

    def mostrar_interface(self):
        
        print("\n" + "=" * 40)

        print(f"🧙 {self.jogador.nome}")
        print(f"Vida   : {self.barra_vida(self.jogador.vida, self.jogador.vida_max)} {self.jogador.vida}/{self.jogador.vida_max}")
        print(f"Elixir : {self.barra(self.jogador.elixir, self.jogador.elixir_max)} {self.jogador.elixir}/{self.jogador.elixir_max}")

        print("\n👾 Inimigo")
        print(f"Vida   : {self.barra_vida(self.inimigo.vida, self.inimigo.vida_max)} {self.inimigo.vida}/{self.inimigo.vida_max}")

        print("=" * 40)

        print("\nEscolha sua ação:")
        print(f"[1] Soco - {self.jogador.forca} dano")
        print(f"[2] Chute - {self.jogador.forca + (self.jogador.forca // 2)} dano (1 elixir)")
        print(f"[3] Ataque com {self.jogador.arma.nome} - {self.jogador.forca + self.jogador.arma.dano} dano (3 elixir)")
        print(f"[4] Ataque Especial - {(self.jogador.forca + self.jogador.arma.dano) * 2} (7 elixir)")
        print("[5] Defender - reduz o dano pela metade")
        print("[6] Curar - restaura 30 HP(4 elixir)")

    def turno_jogador(self):
        while True:
            escolha = input("\nAção: ")
            print("")

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
            if self.jogador.elixir > self.jogador.elixir_max:
                self.jogador.elixir = self.jogador.elixir_max
            if self.inimigo.elixir > self.inimigo.elixir_max:
                self.inimigo.elixir = self.inimigo.elixir_max


        print("\n===== FIM DA BATALHA =====\n")
        if self.jogador.vida > 0:
            print("🏆  VITÓRIA!")
            print(f"""
  ╔══════════════════════════════════════════╗
  ║                                          ║
  ║   {f"{self.jogador.nome} DERROTOU o {self.inimigo.nome}!":<36}   ║
  ║                                          ║
  ║   Vida restante: {f"{self.jogador.vida}":<21}   ║
  ║                                          ║
  ╚══════════════════════════════════════════╝
        """)
        else:
            print("💀  DERROTA...")
            print(f"""
  ╔══════════════════════════════════════════╗
  ║                                          ║
  ║   {f"{self.jogador.nome} foi DERROTADO pelo {self.inimigo.nome}!":<36}   ║
  ║                                          ║
  ║   O {self.inimigo.nome:<10} dança de alegria sobre    ║
  ║   os escombros...                        ║
  ║                                          ║
  ╚══════════════════════════════════════════╝
        """)

    
