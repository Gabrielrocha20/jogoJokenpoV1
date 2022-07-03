import emoji
import random
import time


# import dados


def jokenpo():
    print('BEM VINDO AO')
    apostar = 1000
    casa = 10000
    i = apostar
    while True:
        if apostar <= 0:
            return 'VOCE PERDEU TODAS AS SUAS FICHAS'

        if casa <= 0:
            print('VOCE QUEBROU A BANCA DA CASA')
        if apostar > 0:
            print('=' * 30)
            print((emoji.emojize('\033[1;31m     JO :oncoming_fist:')),
                  (emoji.emojize('\033[1;33m KEN :raised_hand:')), end=' ')
            print(emoji.emojize('\033[1;32m PO :victory_hand:'), '\033[0;0m')
            print('=' * 30)
            print('ESCOLHA!!!')
            print('\033[1;103m\033[1;30m PEDRA[1]\033[0;0m\033[0;0m')
            print('')
            print('\033[1;103m\033[1;30m PAPEL[2]\033[0;0m\033[0;0m')
            print('')
            print('\033[1;103m\033[1;30m TESOURA[3]\033[0;0m\033[0;0m')
            print('Você tem {} fichas digite quanto quer apostar se voce ganhar, ganha 2x'.format(apostar))
            ap = float(input('Quanto voce quer apostar: '))
            if ap < 1.7:
                apostar == apostar
                print('O minimo e 1,70')
                ap = float(input('Quanto voce quer apostar: '))
            if ap > apostar:
                apostar == apostar
                print('Saldo insuficiente')
                ap = float(input('Quanto voce quer apostar: '))
            print('VOCÊ APOSTOU {} fichas SEU NOVO SALDO E DE {}'.format(ap, apostar - ap))
            usuario = int(input('Escolha...: '))
            if usuario > 3:
                print('\033[1;31m \033[1;40m VOCE ESCOLHEU UMA OPÇAO INVALIDA, ESCOLHA ENTRE 1 A 3 '
                      '\033[1;40m \033[0;0m')

            time.sleep(1)
            print((emoji.emojize('\033[1;31m   JO :oncoming_fist:')))
            time.sleep(1)
            print((emoji.emojize('\033[1;33m          KEN :raised_hand:')))
            time.sleep(1)
            print((emoji.emojize('\033[1;32m                   PO :victory_hand:')), '\033[0;0m')
            time.sleep(1)
            maquina = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
            print(f'A MAQUINA ESCOLHEU {maquina}')
            if empate(usuario, maquina):
                casa += ap / 2
                apostar -= ap / 2
                print(apostar, casa)

                print('EMPATE')
            if win(usuario, maquina):
                casa -= ap
                apostar += ap
                print(apostar, casa)
                print('VOCÊ GANHOU!!!')
            if los(maquina, usuario):
                casa += ap
                apostar -= ap
                print(apostar, casa)
                print('VOCÊ PERDEU!!!')
            continuar = input('você quer continuar ? sim ou nao ')
            if continuar == 'sim':
                print('vamos la!')
            else:
                return True


def win(jogador, computador):
    if (jogador == 1 and computador == 'TESOURA') or (jogador == 2 and computador == 'PEDRA') \
            or (jogador == 3 and computador == 'PAPEL'):
        return True


def los(pc, j1):
    if (j1 == 1 and pc == 'PAPEL') or (j1 == 2 and pc == 'TESOURA') \
            or (j1 == 3 and pc == 'PEDRA'):
        return True


def empate(jj1, ppc):
    if (jj1 == 1 and ppc == 'PEDRA') or (jj1 == 2 and ppc == 'PAPEL') or \
            (jj1 == 3 and ppc == 'TESOURA'):
        return True



