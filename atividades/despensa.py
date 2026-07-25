# Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. 
# Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.

lista = ["Açúcar", "Sal", "Biscoito", "Suco", "Manteiga"]

item = input("Digite o item que você quer verificar: ")

if item in lista:
    print(f"O item {item} já está disponível na dispensa. ")
else:
    print(f"O item {item} precisa ser comprado.")


