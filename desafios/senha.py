# Importa o módulo random, utilizado para gerar escolhas aleatórias
import random

# Função responsável por gerar uma senha aleatória
def gerar_senha():

    # String contendo todas as letras maiúsculas
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # String contendo todas as letras minúsculas
    minusculas = "abcdefghijklmnopqrstuvwxyz"

    # String contendo todos os números
    numeros = "0123456789"

    # String contendo alguns caracteres especiais
    especiais = "!@#$%&*"

    # Cria uma lista com pelo menos um caractere de cada categoria
    senha = [
        random.choice(maiusculas),  # Escolhe uma letra maiúscula aleatória
        random.choice(minusculas),  # Escolhe uma letra minúscula aleatória
        random.choice(numeros),     # Escolhe um número aleatório
        random.choice(especiais)    # Escolhe um caractere especial aleatório
    ]

    # Junta todos os caracteres em uma única string
    todos_caracteres = maiusculas + minusculas + numeros + especiais

    # Adiciona mais 8 caracteres aleatórios à senha
    senha.extend(random.choices(todos_caracteres, k=8))

    # Embaralha a ordem dos caracteres da senha
    random.shuffle(senha)

    # Converte a lista em uma única string e a retorna
    return ''.join(senha)

# Chama a função gerar_senha() e exibe a senha gerada
print(f"Senha gerada: {gerar_senha()}")