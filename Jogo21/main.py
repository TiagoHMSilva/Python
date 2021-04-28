import random
from time import sleep


# https://www.alt-codes.net/suit-cards.php
NAIPES = '♠ ♥ ♣ ♦'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
baralho = [(n, c) for c in CARTAS for n in NAIPES]
random.shuffle(baralho)
geral = list()
jogadores = dict()
nova_carta = list()


def distribuir_cartas() -> tuple:
    """Escolhe uma carta aleatoria da lista de batralho e passa para o jogador"""
    carta: tuple = random.choice(baralho)
    baralho.remove(carta)
    return carta


def soma_cartas(cartas) -> int:
    """Função que soma os valores das cartas de cada jogador"""
    cont: int = 0
    for n, v in cartas:
        if v == 'A':
            cont += 1
        elif v == 'J':
            cont += 10
        elif v == 'Q':
            cont += 10
        elif v == 'K':
            cont += 10
        else:
            cont += int(v)
    return cont


def numero_jogadores():
    """Função que cria o dicionario de cada jogadro e joga em uma lista"""
    while True:
        try:
            numerodejogadores: int = int(input('Quantos jogadores(min: 2 max: 6)? '))
        except (ValueError, TypeError):
            print('\033[31mErro\033[m')
        else:
            if 1 < numerodejogadores < 7:
                break
            else:
                print('\033[31mErro\033[m')
    contador : int = 0
    while contador < numerodejogadores:
        jogadores.clear()
        while True:
            nome: str = str(input('Nome do jogador: '))
            if nome.isnumeric() or nome == '':
                print('\033[31mERRO: Por favor entre com um nome valido.\033[m')
            else:
                break
        jogadores['nome'] = nome
        primeira: tuple = distribuir_cartas()
        nova_carta.append(primeira)
        jogadores['cartas'] = nova_carta[:]
        jogadores['soma'] = soma_cartas(jogadores['cartas'])
        geral.append(jogadores.copy())
        contador += 1
        nova_carta.clear()
    quadro_geral(geral)
    menu_jogador(['Comprar uma carta', 'Passar o turno', 'Sair'], 'Menu')


def jogar():
    """Inicia um jogo de cartas"""
    cabecalho('Jogo 21')
    print('Regas do jogo:\033[m\n'
          '\033[34m- Chegar a 21 pontos\n'
          '\033[31m- Se passar de 21 pontos perde\033[m\n'
          '\033[33m- Cada carta tem seu valor\033[m\n'
          '\033[34m- As cartas J, Q, K valem 10 pontos\033[m\n'
          '\033[33m- A carta "A" vale 1 ponto\033[m\n'
          '\033[31m- Limite de cartas por jogador são 3\033[m\n')
    numero_jogadores()


def linha(tam=62):
    """Função que cria uma linha"""
    return '-' * tam


def cabecalho(txt):
    """Função que cria um cabeçalho padronizado"""
    print(linha())
    print(txt.center(62))
    print(linha())


def menu_jogador(vetor, txt, turno: int = 0):
    """Função que fornece ao jogadr suas opções de jogada por turno"""
    while turno != len(geral):
        cabecalho(f'{txt} - jogador: {geral[turno]["nome"]}  cartas : {geral[turno]["cartas"]}')
        contador: int = 0
        for item in vetor:
            print(f'\033[33m{contador+1}\033[m - \033[34m{item}\033[m')
            contador += 1
        print(linha())
        resp_jogador: int = 0
        while resp_jogador == 0:
            resp_jogador: int = readint('\033[33mOpção: \033[m')
            if resp_jogador == 1:
                comprar_carta(turno)
            elif resp_jogador == 2:
                passa_turno()
            elif resp_jogador == 3:
                exit(1)
            else:
                resp_jogador = 0
                print('\033[31mERRO: Entre com uma opção valida.\033[m')
        turno += 1
    quadro_geral(geral)


def quadro_geral(vetor):
    """Função que mostra o quadro de todos os jogadores(nome, cartas na mão e a soma) conferindo se algum jogadr
    ganhou ou perdeu"""
    cabecalho('Menu Geral')
    for i in jogadores.keys():
        print(f'{i:<15}', end='')
    print()
    for k, v in enumerate(vetor):
        print(f' ', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()
    busca: int = 0
    for p in geral:
        soma: int = soma_cartas(geral[busca]['cartas'])
        if soma > 21:
            print(linha())
            print(f'\033[31mO jogador {geral[busca]["nome"]} PERDEUUU!!!! ULTRAPASSOU 21 PONTOS\033[m')
            geral.pop(busca)
            if len(geral) == 1:
                if soma > 21:
                    print(linha())
                    print(f'\033[31mO Nenhum jogador ganhou!!!!\033[m')
                    exit(1)
                else:
                    print(linha())
                    print(f'\033[34mO jogador {geral[busca]["nome"]} GANHOUUU!!!!!\033[m')
                    exit(1)
        if soma == 21:
            print(linha())
            print(f'\033[34mO jogador {geral[busca]["nome"]} GANHOUUU!!!!! CHEGOU AOS 21 PONTOS!!!!\033[m')
            exit(1)
        busca += 1
    menu_jogador(['Comprar carta', 'Passar o turno', 'Sair'], 'Menu')


def readint(numero) -> int:
    """Confere se a resposta do jogador e um número valido"""
    while True:
        try:
            n: int = int(input(numero))
        except (ValueError, TypeError):
            print('\033[31mErro\033[m')
        except KeyboardInterrupt:
            print('\033[31mErro\033[m')
            return 0
        else:
            return n


def passa_turno():
    """O jogador passa sua vez"""
    return 0


def comprar_carta(posicao):
    """Função que escolhe uma carta aleatoria da lista BARALHO e insere na lista da mão do jogador x, se o jogador já
     estiver com a mão cheia(3 cartas) chama a função descartar"""
    pos: int = posicao
    nova_carta.clear()
    cabecalho(f'Cartas - {geral[pos]["nome"]}')
    print(geral[pos]['cartas'], end='')
    print(f' -- soma dadas cadtas : {geral[pos]["soma"]}')
    if (len(geral[pos]["cartas"]) + 1) <= 3:
        nova: tuple = distribuir_cartas()
        geral[pos]['cartas'].append(nova)
        print()
        print(f'Sua nova carta é {nova}')
        geral[pos]['soma'] = soma_cartas(geral[pos]['cartas'])
        print(f' -- soma dadas cadtas : {geral[pos]["soma"]}')
        sleep(1)
    else:
         discartar(posicao)


def discartar(posicao):
    """Função que faz o jogador escolher a posição da carta a ser deescartada na sua lista de cartas na mão"""
    pos: int = posicao
    print()
    print(f'\033[33mJogador alcançou o limite maximo de 3 cartas. Descarte uma carta:\033[m')
    resp_cartas = ['Posição', 'Posição', 'Posição']
    cabecalho(f'Escolha a posição da carta - jogador {geral[pos]["nome"]} ')
    indice: int = 1
    for item in resp_cartas:
        print(f'\033[33m{indice}\033[m - \033[34m{item}\033[m')
        indice += 1
    resp_opcao: int = 0
    while resp_opcao == 0:
        resp_opcao: int = readint('\033[33mOpção: \033[m')
        print(linha())
        if resp_opcao == 1:
            nova: tuple = distribuir_cartas()
            geral[pos]['cartas'][0] = nova
            print(f'Sua nova carta é {nova}')
            print(geral[pos]['cartas'], end='')
            geral[pos]['soma'] = soma_cartas(geral[pos]['cartas'])
            print(f' -- soma dadas cadtas : ', end='')
            print(geral[pos]['soma'])
            sleep(1)
        elif resp_opcao == 2:
            nova: tuple = distribuir_cartas()
            geral[pos]['cartas'][1] = nova
            print(f'Sua nova carta é {nova}')
            print(geral[pos]['cartas'], end='')
            geral[pos]['soma'] = soma_cartas(geral[pos]['cartas'])
            print(f' -- soma dadas cadtas : ', end='')
            print(geral[pos]['soma'])
            sleep(1)
        elif resp_opcao == 3:
            nova: tuple = distribuir_cartas()
            geral[pos]['cartas'][2] = nova
            print(f'Sua nova carta é {nova}')
            print(geral[pos]['cartas'], end='')
            geral[pos]['soma'] = soma_cartas(geral[pos]['cartas'])
            print(f' -- soma dadas cadtas : ', end='')
            print(geral[pos]['soma'])
            sleep(1)
        else:
            resp_opcao = 0
            print('\033[31mERRO: Entre com uma opção valida.\033[m')
            sleep(1)
    quadro_geral(geral)
    menu_jogador(['Comprar carta', 'Passar o turno', 'Sair'], 'Menu', turno=1)


jogar()
