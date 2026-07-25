# À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.

voluntarios = []

while True:   # Inicia um laço infinito. O Python vai repetir esse bloco até encontrar um break.
    nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")  # Pergunta o nome do voluntário e guarda a resposta na variável nome.
    if nome.lower() == 'sair':  # lower() transforma o texto em minúsculas. Então não importa como o usuário vai escrever.
# Se isso acontecer, o break encerra o while.
        break
    voluntarios.append(nome)  # Se o usuário não digitou "sair", o nome é adicionado à lista.
print("\nVoluntários registrados: ", voluntarios)