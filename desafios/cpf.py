# Função responsável por validar um CPF
def validar_cpf(cpf):
    
    if not cpf.isdigit():   # Verifica se o CPF contém apenas números.
        return "Erro: O CPF deve conter apenas números."     # Se houver letras, espaços ou caracteres especiais, retorna uma mensagem de erro.

    
    if len(cpf) != 11:         # Verifica se o CPF possui exatamente 11 dígitos.
        return "Erro: O CPF deve ter exatamente 11 dígitos."  # Caso tenha menos ou mais, retorna uma mensagem de erro.

    # Se passou por todas as verificações acima, o CPF é considerado válido.
    return "CPF válido."

# Solicita ao usuário que digite um CPF.
cpf = input("Digite seu CPF: ")

# Chama a função validar_cpf() passando o CPF digitado
# e imprime o resultado retornado pela função.
print(validar_cpf(cpf))