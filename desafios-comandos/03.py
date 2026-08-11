# Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. 
# Elas querem um programa que mostre: Quais itens apareceram nas duas listas; Quais foram exclusivos de Laura; Quais foram exclusivos da Ana.
# Escreva um programa que solicite as listas e mostre os resultados dessas comparações.


laura = set(input("Lista da Laura: ").split(", "))   # Pede para o usuário digitar os itens da lista da Laura. O split(", ") separa os itens sempre que encontrar ", ". O set transforma os itens em um conjunto e elimina possíveis repetições.


ana = set(input("Lista da Ana: ").split(", "))    # Faz a mesma coisa para a lista da Ana.


comuns = laura.intersection(ana)    # Verifica quais itens aparecem tanto na lista da Laura quanto na lista da Ana. intersection() retorna a interseção entre os dois conjuntos.


exclusivos_laura = laura.difference(ana)   # Pega os itens que estão na lista da Laura, mas que NÃO aparecem na lista da Ana.


exclusivos_ana = ana.difference(laura)   # Pega os itens que estão na lista da Ana,mas que NÃO aparecem na lista da Laura.


print(f"Itens em ambas as listas: {', '.join(comuns)}")  # Exibe os itens que aparecem nas duas listas. O join() junta os elementos do conjunto em uma única string, colocando ", " entre cada item.


print(f"Itens exclusivos de Laura: {', '.join(exclusivos_laura)}") # Exibe somente os itens que pertencem à Laura e não estão na lista da Ana.


print(f"Itens exclusivos de Ana: {', '.join(exclusivos_ana)}")   # Exibe somente os itens que pertencem à Ana e não estão na lista da Laura.
