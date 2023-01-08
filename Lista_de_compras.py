'''

Faça uma lista de comprar com listas
O Usuário deve ter a possibilidade de inserir, apagar, e listar os valores da sua lista
não permita que o programa quebre com erros de índices inexistentes na lista.

'''
from time import sleep
import os
carrinho = []
nome_lista = 'LISTA DE COMPRAS'
valor_total = 0
nome = 'Lista de compras'

print(f'{nome:*^20} \nDigite "s" para Sair \nDigite "a" para Apagar \nDigite "l" para Listar')

while True:
    # verificação se o cliente apertar A apagar ultimo produto e valor.
    try:
        item = input("Digite o nome do item): ") 
        if item == 'a':
            print('Deletando o último item...')
            sleep(2) 
            valor_total -= valor
            del carrinho[-1]
            sleep(0.1)
            os.system('cls')
            print('Último item deletado.')
            print(f'{nome_lista:*^40} ')
            for item, valor in carrinho:
                sleep(0.1)
                print(f'{item:.<30}  R$ {valor:.2f}')
                sleep(0.1)
            print(f'Total: {"-" * 23} R$ {valor_total:.2f}')
            continue   

    # verificação se o cliente apertar L listar

        if item == 'l':
            if carrinho == []:
                print('Carrinho Vazio.')
            else:
                print(f'{nome_lista:*^40} ')
                print('Listando produtos...')
                sleep(1.0)
                os.system('cls')
                print(f'{nome_lista:*^40} ')
                for item, valor in carrinho:
                    sleep(0.1)
                    print(f'{item:.<30}  R$ {valor:.2f}')
                    sleep(0.1)
                print(f'Total: {"-" * 23} R$ {valor_total:.2f}')
                continue

    # verificação se apertar S para sair

        if item == 's':
            print('Encerrando programa...')
            sleep(1)
            print('Programa Encerrado.')
            os.system('cls')
            break
        valor = float(input("Digite o valor do item: "))
        print('produto adicionado')
        sleep(0.2)
        os.system('cls')
        carrinho.append((item, valor))
        valor_total += valor
        print(f'{nome_lista:*^40} ')
        for item, valor in carrinho:
            sleep(0.1)
            print(f'{item:.<30}  R$ {valor:.2f}')
            sleep(0.1)
        print(f'Total: {"-" * 23} R$ {valor_total:.2f}')
        continue

    except ValueError:
        print('Esse não é um valor válido!')
    except IndexError:
        print('Carrinho vazio.')

    
