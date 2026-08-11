# Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.

texto1 = set(input("Texto 1: ").lower().split()) # Recebe o primeiro texto, transforma em minúsculas, separa em palavras com split() e transforma em set.
texto2 = set(input("Texto 2: ").lower().split()) # Faz a mesma coisa com o segundo texto.
comuns = texto1.intersection(texto2)  # intersection() retorna as palavras presentes nos dois conjuntos.
print(f"Palavras em comum: {comuns}")  # Exibe o conjunto de palavras comuns.


