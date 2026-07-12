# Faça um projeto que recebe uma frase e conta quantas vezes cada palavra aparece nela.

def contar_palavras(frase):
    # Chama a função 'limpar_texto' para deixar todas as letras minúsculas
    # e remover os caracteres de pontuação.
    frase = limpar_texto(frase)

    # Verifica se a frase ficou vazia após a limpeza.
    # Se estiver vazia, retorna um dicionário vazio.
    if not frase.strip():
        return {}

    # Divide a frase em uma lista de palavras utilizando os espaços como separador.
    palavras = frase.split()

    # Cria um dicionário vazio que armazenará cada palavra e sua quantidade.
    contagem = {}

    # Percorre cada palavra da lista.
    for palavra in palavras:
        # Se a palavra já existir no dicionário, soma 1 à quantidade.
        # Caso contrário, começa a contagem com 1.
        contagem[palavra] = contagem.get(palavra, 0) + 1

    # Retorna o dicionário com a contagem de todas as palavras.
    return contagem


def limpar_texto(texto):
    # Converte todo o texto para letras minúsculas.
    texto = texto.lower()

    # Define os caracteres de pontuação que serão removidos do texto.
    caracteres = ",.!|?;:'\"()[]{}"

    # Percorre cada caractere da variável 'caracteres'.
    for char in caracteres:
        # Substitui cada caractere encontrado por uma string vazia (""),
        # removendo-o do texto.
        texto = texto.replace(char, "")

    # Retorna o texto já limpo e tratado.
    return texto