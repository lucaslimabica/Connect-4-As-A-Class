# jogo_abs.py
"""
Interface de um jogo para 2 jogadores.
"""

from abc import ABC, abstractmethod
from random import randint


class Jogo(ABC):
    """
    Classe abstrata que define a interface de um jogo para 2 jogadores.
    """

    def __init__(self) -> None:
        """
        Inicializar o jogo.
        """
        print("Bom jogo...")
        self.inicializa_tabuleiro()

    @abstractmethod
    def inicializa_tabuleiro(self) -> None:
        """
        Inicializar o tabuleiro do jogo.
        """
        raise NotImplementedError("A subclasse tem de implementar este método.")

    @abstractmethod
    def mostra_tabuleiro(self) -> None:
        """
        Desenhar o tabuleiro do jogo.
        """
        raise NotImplementedError("A subclasse tem de implementar este método.")

    @abstractmethod
    def joga_humano(self, jogador: int) -> None:
        """
        Solicitar ao humano :jogador: a próxima jogada
        e colocá-la no tabuleiro.
        :param jogador: número do jogador (0 ou 1).
        """
        raise NotImplementedError("A subclasse tem de implementar este método.")

    @abstractmethod
    def joga_computador(self, jogador: int) -> None:
        """
        Realizar a jogada do computador.
        :param jogador: número do jogador (computador).
        """
        raise NotImplementedError("A subclasse tem de implementar este método.")

    @abstractmethod
    def ha_jogadas_possiveis(self) -> bool:
        """
        Verifica se ainda há jogadas possíveis ou se o jogo está empatado.
        :return: `True` se ainda há jogadas possíveis, `False` caso contrário.
        """
        raise NotImplementedError("A subclasse tem de implementar este método.")

    @abstractmethod
    def terminou(self) -> bool:
        """
        Verifica se foi verificada a condição de paragem, i.e., um jogador ganhou.
        :return: `True` se o jogo terminou, `False` caso contrário.
        """
        raise NotImplementedError("A subclasse tem de implementar este método.")

    def jogar(self) -> None:
        """
        Corre o jogo.
        """

        jogador = 0

        # Escolher número do jogador humano
        self.__num_jogador_humano = randint(0, 1)

        while True:
            self.mostra_tabuleiro()

            if jogador == self.__num_jogador_humano:
                self.joga_humano(jogador)
            else:
                self.joga_computador(jogador)

            if self.terminou():
                self.mostra_tabuleiro()
                print(f"\nO jogador {jogador} ganhou!")
                return
            elif not self.ha_jogadas_possiveis():
                self.mostra_tabuleiro()
                print("\nEmpataram...")
                return

            # Passar a vez ao outro jogador
            jogador = (jogador + 1) % 2  # 0->1 ou 1->0