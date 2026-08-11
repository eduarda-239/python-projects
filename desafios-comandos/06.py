# Ana é responsável pelo controle de estoque de uma loja de artigos para papelaria. Ela precisa de um programa que permita cadastrar produtos em forma de dados estruturados. O sistema deve solicitar o nome e a quantidade de três produtos e, ao final, exibir as informações cadastradas em um dicionário, onde cada produto será uma chave e a quantidade correspondente será o valor.

dicionario_produtos = {}
# Cria um dicionário vazio para armazenar os produtos.
# O nome do produto será a chave e a quantidade será o valor.


for i in range(3):
    # Cria um loop que será executado 3 vezes,
    # pois precisamos cadastrar exatamente 3 produtos.

    nome = input("Digite o nome do produto: ")
    # Pede o nome do produto e armazena na variável nome.


    quantidade = int(input("Digite a quantidade: "))
    # Pede a quantidade do produto.
    # input() sempre retorna texto (string), então int()
    # transforma o valor digitado em um número inteiro.


    dicionario_produtos[nome] = quantidade
    # Adiciona o produto ao dicionário.
    # O conteúdo de "nome" será a chave.
    # O conteúdo de "quantidade" será o valor.


print(f"Dicionário de produtos: {dicionario_produtos}")
# Exibe o dicionário completo com os produtos cadastrados.
