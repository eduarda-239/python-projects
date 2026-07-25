# O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto

resultados = ["Ana", "Carlos", "Pedro"]  # Cria-se uma lista com os valores da tal lista
print("Lista original:", resultados)     # Mostra o resultado dos nomes

erro = input("Digite o nome incorreto: ")  # Usuário teria que digitar o nome que ele julga incorreto
if erro in resultados:                    
    correto = input("Digite o nome correto: ")    # Pede para que digite o nome correto
    posicao = resultados.index(erro)              # Ele avalia em qual posição esse nome errado está
    resultados.remove(erro)                       # Remove da lista
    resultados.insert(posicao, correto)           # Insere o nome correto na posição que estava o nome incorreto
    print(f"O nome {erro} foi substituído por {correto}.")    # Exibe a ação que foi feita
    print("Lista atualizada:", resultados)                    # Exibe a lista de nomes atualizada de forma correta
else:
    print("Nome não encontrado.")         # Se ele não achar o nome que o usuário digitou como se fosse o errado ele exibe a mensagem não encontrado