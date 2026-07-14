# Importa o módulo random, utilizado para fazer escolhas aleatórias
import random

# Função responsável por executar o jogo Pedra, Papel e Tesoura
def pedra_papel_tesoura():

    # Lista com as opções possíveis do jogo
    opcoes = ["pedra", "papel", "tesoura"]

    # O computador escolhe aleatoriamente uma das opções
    escolha_computador = random.choice(opcoes)

    # Solicita que o usuário escolha uma opção e converte para letras minúsculas
    escolha_usuario = input("Escolha: pedra, papel ou tesoura? ").lower()

    # Verifica se a escolha do usuário é válida
    if escolha_usuario not in opcoes:
        print("Escolha inválida!")
        return  # Encerra a função caso a escolha seja inválida

    # Exibe a escolha feita pelo computador
    print(f"Computador escolheu: {escolha_computador}")

    # Verifica se houve empate
    if escolha_usuario == escolha_computador:
        print("Empate!")

    # Verifica todas as combinações em que o usuário vence
    elif (
        (escolha_usuario == "pedra" and escolha_computador == "tesoura") or
        (escolha_usuario == "papel" and escolha_computador == "pedra") or
        (escolha_usuario == "tesoura" and escolha_computador == "papel")
    ):
        print("Você venceu!")

    # Se não empatou nem venceu, então o usuário perdeu
    else:
        print("Você perdeu!")

# Chama a função para iniciar o jogo
pedra_papel_tesoura()