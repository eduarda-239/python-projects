# Função principal do caixa eletrônico
def caixa_eletronico():

    # Lista contendo os valores das cédulas disponíveis
    cedulas = [100, 50, 20, 10, 5, 2]

    try:
        # Solicita ao usuário o valor que deseja sacar
        valor = int(input("Digite o valor do saque: "))

        # Verifica se o valor é maior que zero
        if valor <= 0:
            print("Erro: O valor deve ser positivo.")

        # Verifica se o valor é múltiplo de 2
        # Como não existe cédula de R$ 1, não é possível sacar valores ímpares
        elif valor % 2 != 0:
            print("Erro: O valor deve ser múltiplo de 2.")

        else:
            # Exibe a mensagem indicando que as cédulas serão apresentadas
            print("Cédulas entregues:")

            # Percorre cada valor de cédula disponível
            for cedula in cedulas:

                # Calcula quantas cédulas daquela denominação serão utilizadas
                quantidade = valor // cedula

                # Verifica se será utilizada pelo menos uma cédula
                if quantidade > 0:

                    # Exibe a quantidade de cédulas daquela denominação
                    print(f"{quantidade} cédulas de R$ {cedula}")

                    # Atualiza o valor restante do saque
                    valor = valor % cedula

    # Captura erro caso o usuário digite algo que não seja um número inteiro
    except ValueError:
        print("Erro: Digite um valor numérico válido.")

# Chama a função para iniciar o programa
caixa_eletronico()