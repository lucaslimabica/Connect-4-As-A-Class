from jogo_abs import Jogo
from random import randint
from pyfiglet import figlet_format


class Quatro_Em_Linha(Jogo):
    def inicializa_tabuleiro(self) -> None:
        """
        Inicializa o tabuleiro 7x7 do jogo,
        numa disposição de lista de listas.
        """
        self.icons = ["X", "O"]
        self.linhas_tab = 7
        self.colunas_tab = 7
        # Um array de arrays a serem preenchidos
        self.tabuleiro = [
            ["-" for i in range(self.linhas_tab)] for i in range(self.colunas_tab)
        ]

    def mostra_tabuleiro(self) -> None:
        """
        Desenha o tabuleiro do jogo.
        """
        for linha in self.tabuleiro:
            print(" | ".join(linha))
            print("-" * 26)

    def validar_jogada(self, play: int) -> bool:
        """
        Retorna True se a jogada realizada
        estiver nas regras do jogo, caso contrário,
        irá ficar num loop a solicitar uma nova jogada.
        """
        jogadas_validas = [0, 1, 2, 3, 4, 5, 6]

        if play in jogadas_validas and self.tabuleiro[0][play] == "-":
            return True
        else:
            print("Jogada inválida! Tente novamente!")
            return False

    def joga_humano(self) -> None:
        """
        Solicita ao humano a próxima jogada
        e coloca-a no tabuleiro.
        """
        while True:
            col = int(input(f"Jogador {self.icons[0]} escolha uma coluna:")) - 1
            if self.validar_jogada(col) is True:
                break

        for linha in range(
            self.linhas_tab - 1, -1, -1
        ):  # Começamos do fundo até o index (que é o topo), escalando de -1 em -1
            if (
                self.tabuleiro[linha][col] == "-"
            ):  # Achou o primeiro espaço vazio
                self.tabuleiro[linha][col] = self.icons[0]
                break


    def joga_computador(self) -> None:
        """
        Faz uma jogada aleatória para a máquina.
        """
        print("GLaDOS jogará...")
        while True:
            col = randint(0, 6)

            # Um if para validar a jogada
            if self.tabuleiro[0][col] != "-":
                # O topo da coluna está preenchido
                col = randint(0, 6)
            else:
                break

        for linha in range(self.linhas_tab - 1, -1, -1):
            if self.tabuleiro[linha][col] == "-":  # Achou o primeiro espaço vazio
                self.tabuleiro[linha][col] = self.icons[1]
                break

    def ha_jogadas_possiveis(self) -> bool:
        """
        verifica se há alguma casa em branco.
        """
        casas_vazias = 0
        for linha in self.tabuleiro:
            casas_vazias = casas_vazias + linha.count("-")

        if casas_vazias == 0:
            return True
        else:
            return False

    def win_Diagonal(self) -> bool:
        """
        Valida se há diagonais iguais.
        """

        # Para se calcular diagonais para o canto superior direito, usamos a fórmula:
        # (linha, coluna), (linha - 1, coluna + 1), (linha - 2, coluna + 2), (linha - 3, coluna + 3)
        # Pois uma diagonal assim, sobe, avança em linha e coluna

        for linha in range(3, self.linhas_tab):
            for coluna in range(0, 4):
                if (
                    self.tabuleiro[linha][coluna] != "-"
                ):  # Não procuramos por diagonais vazias
                    if (
                        self.tabuleiro[linha][coluna]
                        == self.tabuleiro[linha - 1][coluna + 1]
                        == self.tabuleiro[linha - 2][coluna + 2]
                        == self.tabuleiro[linha - 3][coluna + 3]
                    ):
                        return True

        # Para se calcular diagonais para o canto inferior direito, usamos a fórmula:
        # (linha, coluna), (linha + 1, coluna + 1), (linha + 2, coluna + 2), (linha + 3, coluna + 3)
        # Pois uma diagonal assim, desce, diminui em linha e aumenta em coluna

        for linha in range(0, 4):
            for coluna in range(0, 4):
                if (
                    self.tabuleiro[linha][coluna] != "-"
                ):  # Não procuramos por diagonais vazias
                    if (
                        self.tabuleiro[linha][coluna]
                        == self.tabuleiro[linha + 1][coluna + 1]
                        == self.tabuleiro[linha + 2][coluna + 2]
                        == self.tabuleiro[linha + 3][coluna + 3]
                    ):
                        return True

        return False

    def win_Horizontal(self) -> bool:
        """
        Valida se há horizontais iguais.
        """
        for linha in range(0, self.linhas_tab):
            for coluna in range(0, 4):
                if (
                    self.tabuleiro[linha][coluna] != "-"
                ):  # Não procuramos por horizontais vazias
                    if (
                        self.tabuleiro[linha][coluna]
                        == self.tabuleiro[linha][coluna + 1]
                        == self.tabuleiro[linha][coluna + 2]
                        == self.tabuleiro[linha][coluna + 3]
                    ):
                        return True
            for coluna in range(6, 2, -1):
                if self.tabuleiro[linha][coluna] != "-":
                    if (
                        self.tabuleiro[linha][coluna]
                        == self.tabuleiro[linha][coluna - 1]
                        == self.tabuleiro[linha][coluna - 2]
                        == self.tabuleiro[linha][coluna - 3]
                    ):
                        return True

        return False

    def win_Vertical(self) -> bool:
        """
        Verifica se há linhas verticais iguais.
        """
        for linha in range(0, 4):
            for coluna in range(0, self.colunas_tab):
                if (
                    self.tabuleiro[linha][coluna] != "-"
                ):  # Não procuramos por verticais vazias
                    if (
                        self.tabuleiro[linha][coluna]
                        == self.tabuleiro[linha + 1][coluna]
                        == self.tabuleiro[linha + 2][coluna]
                        == self.tabuleiro[linha + 3][coluna]
                    ):
                        return True

            for coluna in range(6, 2, -1):
                if self.tabuleiro[linha][coluna] != "-":
                    if (
                        self.tabuleiro[linha][coluna]
                        == self.tabuleiro[linha + 1][coluna]
                        == self.tabuleiro[linha + 2][coluna]
                        == self.tabuleiro[linha + 3][coluna]
                    ):
                        return True

        return False

    def win(self) -> bool:
        """
        Executa todos os métodos win.
        """
        if self.win_Diagonal():
            return True

        elif self.win_Horizontal():
            return True

        elif self.win_Vertical():
            return True

        return False

    def terminou(self, jogador: int) -> bool:
        """
        Irá validar se o jogo acabou.
        """
        if self.win():
            print(f"Fim de Jogo! Vitória do jogador {self.icons[jogador]}")
            return True
        elif self.ha_jogadas_possiveis():
            print("Fim de Jogo! Empate!")
            return True
        else:
            return False

    def jogar(self):
        """
        Estrutura do jogo.
        """
        print("-=-" * 10)
        print(figlet_format("Quatro\nEm Linha\n"))
        print("-=-" * 10)
        self.inicializa_tabuleiro()
        self.mostra_tabuleiro()
        for vez in range(self.linhas_tab * self.colunas_tab):
            # Número possível de vezes a se jogar
            self.joga_humano()
            self.mostra_tabuleiro()
            if self.terminou(0):
                break
            else:
                self.joga_computador()
                self.mostra_tabuleiro()
            if self.terminou(1):
                break


if __name__ == "__main__":
    jogo = Quatro_Em_Linha()
    jogo.jogar()