import os
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    
    print('Tarefas')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        listar(tarefas)
        print('Nenhuma tarefa para Desfazer')
        return

    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print(f'{tarefa} Removida da lista. ')


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para Resfazer')
        return

    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma Tarefa')
        return

    tarefas.append(tarefa)
    print(f'{tarefa} Adicionada na lista. ')
    print()


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer') # oferece opções ao usuário
    tarefa = input('Digite uma tarefa ou comando: ') # pede ao usuário uma informação

    if tarefa == 'listar':
        listar(tarefas)

    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)

    elif tarefa == 'clear':
        os.system('cls')
        
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
