# Ana percebeu que, após o cadastro inicial dos produtos, precisa atualizar a quantidade de um item específico no estoque. 
# Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, atualizando essa informação no dicionário de estoque.

estoque = {
    "Caderno universitário": 50,
    "Caneta azul": 120,
    "Borracha branca": 30
}
# Cria um dicionário com os produtos como chaves
# e suas respectivas quantidades como valores.


produto = input("Digite o nome do produto a ser atualizado: ")
# Pede ao usuário o nome do produto que ele deseja atualizar.


nova_quantidade = int(input("Digite a nova quantidade: "))
# Pede a nova quantidade.
# int() transforma o valor digitado, que inicialmente é uma string,
# em um número inteiro.


if produto in estoque:
    # Verifica se o produto digitado existe como uma chave no dicionário.


    estoque[produto] = nova_quantidade
    # Se o produto existir, substitui a quantidade antiga
    # pela nova quantidade.


    print("Quantidade atualizada com sucesso!")
    # Informa que a atualização foi realizada.


    print(estoque)
    # Exibe o dicionário atualizado.


else:
    # Se o produto não existir no dicionário...


    print("Produto não encontrado no estoque.")
    # Informa que o produto não foi encontrado.

