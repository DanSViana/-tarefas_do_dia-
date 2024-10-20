'''
Crie um programa em que o usuário possa cadastrar uma lista de tarefas a fazer no dia. Após terminar, envie o link do repositório no GitHub.
'''

# lista de tarefas
tarefas = []

while True:
    # lista 
    print('1 - Crie uma nova tarefa.')
    print('2 - Exibir lista de tarefas.')
    print('3 - Encerrar programa.')

    # Escolha do usuário
    opcao = input('\nOpção do usuário:')

    # verifica a opção escolhida
    match opcao:
        case '1':
            nova_tarefa = input('Crie uma nova tarefa:').capitalize()
            tarefas.append(nova_tarefa)
            print(f'{nova_tarefa} Tarefa inserida com sucesso.')
            continue
        case '2':
            print('\n LISTA DE TAREFAS:\n')
            for tarefa in tarefas:
                print(tarefa)
            continue
        case '3':
            tarefas.sort()
            for tarefa in tarefas:
                print(tarefas)
                print('Nova lista')
            break
        case _:
            print('Opção Inválida')