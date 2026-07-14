# Função que conta a quantidade de vogais em um texto
def contar_vogais(texto):

    # String contendo todas as vogais que serão verificadas
    vogais = "aeiou"

    # Variável que armazenará a quantidade de vogais encontradas
    quantidade = 0

    # Percorre cada letra do texto convertido para minúsculas
    for letra in texto.lower():

        # Verifica se a letra atual é uma vogal
        if letra in vogais:

            # Se for uma vogal, incrementa o contador
            quantidade += 1

    # Retorna a quantidade total de vogais encontradas
    return quantidade


# Solicita que o usuário digite um texto
texto = input("Digite um texto: ")

# Chama a função contar_vogais() e exibe o resultado
print(f"O texto contém {contar_vogais(texto)} vogais.")