from contador import contar_palavras   # Importa a função 'contar_palavras' do arquivo contador.py.

frase = input("Digite uma frase: ").strip()  # Solicita uma frase ao usuário, remove espaços no início e no fim e armazena o resultado na variável 'frase'.

if not frase:   # Verifica se o usuário não digitou nenhuma frase.
    print("Erro: Nenhuma frase foi digitada.")   # Exibe uma mensagem de erro caso a entrada esteja vazia.
else:
    resultado = contar_palavras(frase)   # Chama a função 'contar_palavras' e armazena o dicionário retornado.

    if resultado:   # Verifica se o dicionário possui palavras válidas.
        print("Contagem de Palavras: ")   # Exibe um título antes da lista de palavras.

        for palavra, quantidade in resultado.items():   # Percorre cada par (palavra, quantidade) do dicionário.
            print(f"{palavra}: {quantidade}")   # Exibe a palavra e o número de vezes que ela aparece na frase.

    else:
        print("Nenhuma palavra válida foi encontrada.")   # Exibe uma mensagem caso nenhuma palavra válida seja encontrada.