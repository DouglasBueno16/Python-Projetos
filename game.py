"""
Desenvolver uma aplicação onde, ao ser inicializada solicita ao usuário, que escolha um nível
de dificuldade do jogo.
Com a dificuldade selecionada, apresenta de forma aleatória um cálculo, para o usuário informe o
resultado.

Opcões de cálculo:
    -Soma: +
    -Subtração: -
    -Multiplicação: *
    -Divisão: /

Caso o usuário acerte a resposta, será somado 1 ponto no placar
Acertando ou errando, poderá continuar no jogo.
"""
from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejada [1, 2, 3, 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1  # Pontos recebe o valor de pontos + 1
        print(f'Você tem {pontos} pontos.')

    continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não]: '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} pontos. \nAté a próxima!')


if __name__ == '__main__':
    main()
