# Ajude Paulo criando um programa que automatize essa operação, permitindo listar os pedidos e remover o último item automaticamente.
# Ex de entrada: Pedidos feitos (separados por vírgula): Sanduíche, Suco, Sobremesa
# Ex de saída: Pedidos finais: ['Sanduíche', 'Suco']

pedidos = input("Digite os pedidos feitos (separados por vírgula): ").split(", ")
pedidos.pop()   # Remove o último elemento da lista e o descarta
print("Pedidos finais:")
print(pedidos)
