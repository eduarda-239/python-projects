# Como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?
# Exemplo de entrada:
# Produtos do estoque 1 (separados por vírgula): Arroz, Feijão, Macarrão
# Produtos do estoque 2 (separados por vírgula): Óleo, Sal, Açúcar

estoque1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
estoque2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))
estoque_combinado = estoque1 + estoque2  
print(f"Estoque combinado:\n{estoque_combinado}")