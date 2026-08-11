# Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram do evento. 
# O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante. 
# O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista.


participantes = {
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"},
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"}
}
# Cria um dicionário chamado participantes.
# Cada chave é o nome de um workshop.
# O valor de cada chave é um set contendo os nomes dos participantes.


nome_remover = input("Digite o nome do participante a ser removido: ")
# Pede ao usuário o nome do participante que deseja remover.
# O nome digitado fica armazenado na variável nome_remover.


for workshop, nomes in participantes.items():
    # .items() permite acessar a chave e o valor do dicionário ao mesmo tempo.
    # workshop recebe o nome do workshop.
    # nomes recebe o set de participantes daquele workshop.
    # O for passa por todos os workshops.


    nomes.discard(nome_remover)
    # Tenta remover o participante do set daquele workshop.
    # Se o nome existir, ele será removido.
    # Se o nome NÃO existir, nada acontece e o programa continua normalmente.


print("Lista atualizada de participantes:")
# Exibe uma mensagem antes de mostrar os participantes atualizados.


for workshop, nomes in participantes.items():
    # Percorre novamente todos os workshops e seus respectivos sets.


    print(f"{workshop}: {nomes}")
    # Exibe o nome do workshop e o conjunto atualizado de participantes.
