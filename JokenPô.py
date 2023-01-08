# pedra papel tesoura
import random
from time import sleep

itens = ('Sair', 'Pedra', 'Papel', 'Tesoura')
print('-=' * 15)
print('-=' * 15)
placarJ = 0
placarC = 0
contador = 0
sair = False
while contador <= 10:
    try:
        computador = random.randint(1, 3)  # randomizar de tanto a tanto
        jogador = int(input('Escolha sua opção: \n[1] - Pedra \n[2] - Papel \n[3] - Tesoura \n[0] - Sair \n>> '))
        if jogador == 0:
            print('Carregando placar...')
            sleep(3)
            print(f'JOGADOR {placarJ} vs {placarC} COMPUTADOR')
            sair = True
            print('Você saiu do jogo!')
            break
        elif computador == 1:  # computador jogou PEDRA#
            if jogador == 1:
                print('você escolheu: {}'.format(itens[jogador]))
                print('JO!')
                sleep(1)
                print('KEN!')
                sleep(1)
                print('PO!')
                sleep(1)
                print('-=' * 10)
                print('Empate!')
                print('-=' * 10)
                sleep(2)
                print('computador escolheu: {}'.format(itens[computador]))
                print('-=' * 10)
                print('O placar é JOGADOR {} VS {} COMPUTADOR'.format(placarJ, placarC))
            elif jogador == 2:
                print('você escolheu: {}'.format(itens[jogador]))
                placarJ += 1
                print('JO!')
                sleep(1)
                print('KEN!')
                sleep(1)
                print('PO!')
                sleep(1)
                print('-=' * 10)
                print('O Jogador Ganhou!')
                print('-=' * 10)
                sleep(2)
                print('computador escolheu: {}'.format(itens[computador]))
                print('-=' * 10)
                print('O placar é JOGADOR {} VS {} COMPUTADOR'.format(placarJ, placarC))
            elif jogador == 3:
                print('você escolheu: {}'.format(itens[jogador]))
                placarC += 1
                print('JO!')
                sleep(1)
                print('KEN!')
                sleep(1)
                print('PO!')
                sleep(1)
                print('-=' * 10)
                print('O Computador Ganhou!')
                print('-=' * 10)
                sleep(2)
                print('computador escolheu: {}'.format(itens[computador]))
                print('-=' * 10)
                print('O placar é JOGADOR {} VS {} COMPUTADOR'.format(placarJ, placarC))
            else:
                print('Jogada Inválida.')
        elif computador == 2:  # computador jogou PAPEL
            if jogador == 1:
                print('você escolheu: {}'.format(itens[jogador]))
                placarC += 1
                print('JO!')
                sleep(1)
                print('KEN!')
                sleep(1)
                print('PO!')
                sleep(1)
                print('-=' * 10)
                print('O Computador Ganhou!')
                print('-=' * 10)
                sleep(2)
                print('computador escolheu: {}'.format(itens[computador]))
                print('-=' * 10)
                print('O placar é JOGADOR {} VS {} COMPUTADOR '.format(placarJ, placarC))
            elif jogador == 2:
                print(' você escolheu: {}'.format(itens[jogador]))
                print('JO!')
                sleep(1)
                print('KEN!')
                sleep(1)
                print('PO!')
                sleep(1)
                print('-=' * 10)
                print('Empate!')
                print('-=' * 10)
                sleep(2)
                print('computador escolheu: {}'.format(itens[computador]))
                print('-=' * 10)
                print('O placar é JOGADOR {} VS {} COMPUTADOR '.format(placarJ, placarC))
            elif jogador == 3:
                print('você escolheu: {}'.format(itens[jogador]))
                placarJ += 1
                print('JO!')
                sleep(1)
                print('KEN!')
                sleep(1)
                print('PO!')
                sleep(1)
                print('-=' * 10)
                print('O Jogador Ganhou!')
                print('-=' * 10)
                sleep(2)
                print('computador escolheu: {}'.format(itens[computador]))
                print('-=' * 10)
                print('O placar é JOGADOR {} VS {} COMPUTADOR'.format(placarJ, placarC))
            else:
                print('Jogada Inválida.')
        elif computador == 3:  # computador jogou TESOURA
            if jogador == 1:
                print('você escolheu: {}'.format(itens[jogador]))
                placarJ += 1
                print('JO!')
                sleep(1)
                print('KEN!')
                sleep(1)
                print('PO!')
                sleep(1)
                print('-=' * 10)
                print('O Jogador Ganhou!')
                print('-=' * 10)
                sleep(2)
                print('O computador escolheu: {}'.format(itens[computador]))
                print('-=' * 10)
                print('O placar é  JOGADOR {} VS {} COMPUTADOR '.format(placarJ, placarC))
            elif jogador == 2:
                print('você escolheu: {}'.format(itens[jogador]))
                placarC += 1
                print('JO!')
                sleep(1)
                print('KEN!')
                sleep(1)
                print('PO!')
                sleep(1)
                print('-=' * 10)
                print('O Computador Ganhou!')
                print('-=' * 10)
                sleep(2)
                print('computador escolheu: {}'.format(itens[computador]))
                print('-=' * 10)
                print('O placar é JOGADOR {} VS {} COMPUTADOR'.format(placarJ, placarC))
            elif jogador == 3:
                print('você escolheu: {}'.format(itens[jogador]))
                print('JO!')
                sleep(1)
                print('KEN!')
                sleep(1)
                print('PO!')
                sleep(1)
                print('-=' * 10)
                print('Empate!')
                print('-=' * 10)
                sleep(2)
                print('computador escolheu: {}'.format(itens[computador]))
                print('-=' * 10)
                print('O placar é JOGADOR {} VS {} COMPUTADOR'.format(placarJ, placarC))
            else:
                print('Jogada Inválida.')

    except ValueError:
        print('você só pode digitar números de 0 até 3!')