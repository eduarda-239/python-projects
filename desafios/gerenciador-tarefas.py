
# Função principal do gerenciador de tarefas
def gerenciador_tarefas():

    # Cria uma lista vazia para armazenar as tarefas
    tarefas = []

    # Loop principal do programa, que será executado até o usuário escolher sair
    while True:

        # Exibe o menu de opções
        print("\n1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")

        # Solicita que o usuário escolha uma opção
        opcao = input("Escolha uma opção: ")

        # Opção para adicionar uma nova tarefa
        if opcao == "1":

            # Solicita a descrição da tarefa e remove espaços extras do início e do fim
            tarefa = input("Digite a tarefa: ").strip()

            # Verifica se o usuário digitou alguma coisa
            if tarefa:

                # Adiciona a tarefa à lista
                tarefas.append(tarefa)

                # Informa que a tarefa foi adicionada com sucesso
                print("Tarefa adicionada!")

            else:
                # Exibe uma mensagem caso o usuário deixe a tarefa em branco
                print("Erro: A tarefa não pode estar vazia.")

        # Opção para visualizar todas as tarefas
        elif opcao == "2":

            # Verifica se existe pelo menos uma tarefa cadastrada
            if tarefas:

                print("\nTarefas:")

                # Percorre a lista exibindo o número e a descrição de cada tarefa
                # enumerate() gera o índice e a tarefa, começando a contagem em 1
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")

            else:
                # Caso não existam tarefas cadastradas
                print("Nenhuma tarefa cadastrada.")

        # Opção para remover uma tarefa
        elif opcao == "3":

            # Verifica se há tarefas cadastradas
            if not tarefas:
                print("Erro: Nenhuma tarefa para remover.")
                continue  # Volta para o início do menu

            try:
                # Solicita o número da tarefa e ajusta o índice para começar em 0
                indice = int(input("Digite o número da tarefa a ser removida: ")) - 1

                # Verifica se o índice informado existe na lista
                if 0 <= indice < len(tarefas):

                    # Remove a tarefa da lista e armazena seu conteúdo
                    removida = tarefas.pop(indice)

                    # Exibe a tarefa removida
                    print(f"Tarefa '{removida}' removida!")

                else:
                    # Caso o número informado seja inválido
                    print("Erro: Índice inválido! Digite um número válido.")

            # Captura erro caso o usuário digite letras em vez de números
            except ValueError:
                print("Erro: Entrada inválida! Digite um número.")

        # Opção para encerrar o programa
        elif opcao == "4":

            print("Saindo do gerenciador de tarefas. Até mais!")

            # Encerra o loop
            break

        # Caso o usuário digite uma opção inexistente
        else:
            print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")

# Chama a função para iniciar o gerenciador de tarefas
gerenciador_tarefas()