import random

jogador = int(input(
    'Escolha uma opção (1,2,3 ou 4): 1-Pedra  2-Papel  3-Tesoura e  4-Sair: '))

maquina = random.randint(1, 3)

while jogador == maquina:

    tesoura = 0
    pedra = 0
    papel = 0

    if jogador == 1 and papel != 10:
        papel = papel+1
    elif jogador == 2 and tesoura != 10:
        tesoura = tesoura+1
    elif jogador == 3 and pedra != 10:
        pedra = pedra+1

    print("Empate")
    jogador = int(input(
        'Escolha novamente uma opção (1,2,3 ou 4): 1-Pedra  2-Papel  3-Tesoura e  4-Sair: '))
    if jogador == 4:
        break
    maquina = int(
        (random.choices([1, 2, 3], weights=[pedra, papel, tesoura]))[0])


def jogada(jog, maq):
    if jog == 1:
        print("Sua Jogada: Pedra")
        if maq == 2:
            print("Jogada da Maquina: Papel")
            print("Derrota")
        elif maq == 3:
            print("Jogada da Maquina: Tesoura")
            print("Vitória")
    elif jog == 2:
        print("Sua Jogada: Papel")
        if maq == 1:
            print("Jogada da Maquina: Pedra")
            print("Vitória")
        elif maq == 3:
            print("Jogada da Maquina: Tesoura")
            print("Derrota")
    elif jog == 3:
        print("Sua Jogada: Tesoura")
        if maq == 1:
            print("Jogada da Maquina: Pedra")
            print("Derrota")
        elif maq == 2:
            print("Jogada da Maquina: Papel")
            print("Vitória")


jogada(jogador, maquina)
