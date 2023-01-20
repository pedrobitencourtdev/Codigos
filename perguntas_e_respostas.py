'''
# Exercício - sistema de perguntas e respostas
'''
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1', '2', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5',
        'Opções': ['25', '55', '10', '51', '25'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },

]
contador = 0
acertou = 0
# acessando dicionários dentro das listas.
while True:
    for pergunta in perguntas:
        print('Pergunta:', pergunta['Pergunta'])
        print()
        for i, opcao in enumerate(pergunta['Opções']): # para pegar índices uso enumerate.
            print(f'{i})', opcao)
        print()

        # Pedir a opção do cliente
        escolha = input('Escolha uma opção: ')

        if escolha == '3':
            print('Acertou')
            acertou += 1
            contador += 1
        elif escolha == '4':
            print('Acertou')
            acertou += 1
            contador += 1
        elif escolha == '1':
            print('Acertou')
            acertou += 1
            contador += 1
        else:
            print('Errou!')
            acertou -= 1
        if acertou < 0:
            acertou = 0

    print(f'Você acertou {acertou} de 3 Perguntas.')
    jogar_denovo = input('Quer jogar novamente? S/N ')
    if jogar_denovo == 's'.strip():
        contador = 0
        acertou = 0
        continue
    else:
        break
    
