from Models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    print('-' * 60)
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))
    calc: Calcular = Calcular(dificuldade)
    print()
    print('Informe o resultado para a seguinte operação: ')
    print()
    calc.mostrar_operacao()
    resltado: int = int(input())
    if calc.checar_resultado(resltado):
        pontos += 1
        print()
        print(f'Você tem {pontos} ponto(s).')
        print()
    continuar: int = int(input('Deseja continuar no jogo? [1- Sim/ 0- Não] '))
    if continuar:
        jogar(pontos)
    else:
        print('-' * 60)
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até a próxima!')


if __name__ == '__main__':
    print('-' * 60)
    print('Jogo da Matemática'.center(60))
    main()
