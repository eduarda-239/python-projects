# Função que realiza a soma de dois números
def somar(num1, num2):
    return num1 + num2

# Função que realiza a subtração de dois números
def subtrair(num1, num2):
    return num1 - num2

# Função que realiza a multiplicação de dois números
def multiplicar(num1, num2):
    return num1 * num2

# Função que realiza a divisão de dois números
def dividir(num1, num2):

    # Verifica se o divisor é igual a zero
    if num2 == 0:

        # Gera uma exceção caso o usuário tente dividir por zero
        raise ZeroDivisionError

    # Retorna o resultado da divisão
    return num1 / num2

# Função principal da calculadora
def calculadora():
    try:
        # Solicita o primeiro número ao usuário
        num1 = float(input("Digite o primeiro número: "))

        # Solicita qual operação matemática será realizada
        operacao = input("Escolha a operação (+, -, *, /): ")

        # Solicita o segundo número ao usuário
        num2 = float(input("Digite o segundo número: "))

        # Verifica qual operação foi escolhida e chama a função correspondente
        if operacao == "+":
            resultado = somar(num1, num2)

        elif operacao == "-":
            resultado = subtrair(num1, num2)

        elif operacao == "*":
            resultado = multiplicar(num1, num2)

        elif operacao == "/":
            resultado = dividir(num1, num2)

        # Caso o usuário digite uma operação inexistente
        else:
            print("Operação inválida!")
            return

        # Exibe o resultado da operação
        print(f"Resultado: {resultado}")

    # Captura erro caso o usuário digite algo que não seja um número
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")

    # Captura erro de divisão por zero
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")

# Chama a função para iniciar a calculadora
calculadora()