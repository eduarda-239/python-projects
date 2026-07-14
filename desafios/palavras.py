# Solicita que o usuário digite um texto
texto = input("Digite um texto: ")

# Cria uma lista vazia para armazenar as palavras com mais de 10 caracteres
palavras_longas = []

# Percorre cada palavra do texto.
# O método split() separa o texto em palavras usando os espaços como separador.
for palavra in texto.split():

    # Verifica se a palavra possui mais de 10 caracteres
    if len(palavra) > 10:

        # Adiciona a palavra à lista de palavras longas
        palavras_longas.append(palavra)

# Verifica se a lista de palavras longas não está vazia
if palavras_longas:

    # Exibe uma mensagem informando que foram encontradas palavras longas
    print("Palavras longas encontradas:")

    # Percorre a lista de palavras longas e imprime cada uma delas
    for palavra in palavras_longas:
        print(palavra)
else:

    # Caso nenhuma palavra longa tenha sido encontrada, exibe esta mensagem
    print("Nenhuma palavra longa foi encontrada no texto.")
