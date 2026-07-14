# Importa o módulo random, utilizado para gerar números aleatórios
import random

# Função responsável pelo jogo de adivinhar o número
def adivinhar_numero():

    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)

    # Variável para contar quantas tentativas o usuário fez
    tentativas = 0

    # Loop que continua até o usuário acertar o número
    while True:
        try:
            # Solicita um palpite ao usuário e converte para inteiro
            palpite = int(input("Tente adivinhar o número (1-100): "))

            # Verifica se o número informado está entre 1 e 100
            if not 1 <= palpite <= 100:

                # Gera uma exceção caso o número esteja fora do intervalo permitido
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")

            # Incrementa o contador de tentativas
            tentativas += 1

            # Verifica se o palpite foi menor que o número secreto
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")

            # Verifica se o palpite foi maior que o número secreto
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")

            # Se não é menor nem maior, então o usuário acertou
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")

                # Encerra o loop
                break

        # Captura erros de entrada, como letras ou números fora do intervalo
        except ValueError as e:
            print(f"Entrada inválida: {e}")

# Chama a função para iniciar o jogo
adivinhar_numero()