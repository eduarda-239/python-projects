# Nathalia é gerente de uma loja virtual e precisa de um sistema que receba os registros de vendas organizados por categoria de produto. 
# Cada categoria contém uma lista de dicionários representando as vendas individuais, com informações sobre o produto, a quantidade vendida e o valor unitário. 
# Sua tarefa é criar um programa que exiba o total de vendas por categoria.


vendas = {
    "Eletrônicos": [
        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000},
        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500}
    ],
    # Cria a categoria "Eletrônicos".
    # Dentro dela existe uma lista com os produtos vendidos.
    # Cada produto é representado por um dicionário.
    # Cada dicionário possui produto, quantidade e valor_unitario.

    "Eletrodomésticos": [
        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000},
        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800}
    ],
    # Cria a categoria "Eletrodomésticos".
    # Assim como em Eletrônicos, existe uma lista contendo
    # dicionários com as informações de cada venda.

    "Livros": [
        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50},
        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100}
    ]
    # Cria a categoria "Livros" com suas respectivas vendas.
}

print("Total de vendas por categoria:")
# Exibe um título antes de mostrar os resultados.


for categoria, itens in vendas.items():
    # Percorre o dicionário vendas.
    # .items() permite pegar a chave e o valor ao mesmo tempo.
    # categoria recebe o nome da categoria.
    # itens recebe a lista de produtos daquela categoria.


    total = 0
    # Cria a variável total começando em 0.
    # Ela será usada para somar o valor de todas as vendas
    # daquela categoria.


    for item in itens:
        # Percorre cada produto dentro da lista da categoria.
        # A variável item recebe cada dicionário de produto.


        total += item["quantidade"] * item["valor_unitario"]
        # Acessa a quantidade do produto usando ["quantidade"].
        # Acessa o valor unitário usando ["valor_unitario"].
        # Multiplica quantidade × valor unitário.
        # Depois adiciona o resultado ao total.
        #
        # Exemplo:
        # Smartphone: 5 × 2000 = 10000
        # Tablet: 3 × 1500 = 4500
        # Total de Eletrônicos: 14500


    print(f"- {categoria}: R$ {total:.2f}")
    # Mostra o nome da categoria e o total calculado.
    # :.2f significa que o número será exibido com 2 casas decimais.

