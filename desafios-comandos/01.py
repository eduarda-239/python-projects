# Ana está organizando uma festa de aniversário e precisa de uma lista de convidados que não tenha repetições. Ela gostaria que o programa solicitasse o nome dos convidados e, ao final, exibisse a lista organizada sem repetições.
# Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final mostre a lista de convidados sem repetições.

convidados = set()  # Cria um conjunto vazio para armazenar os nomes dos convidados. O set não permite nomes repetidos.

while True:  # Cria um loop que continuará executando até encontrar um break.

    nome = input("Digite o nome do convidado ou 'sair' para encerrar: ") # Pede para o usuário digitar um nome e armazena o que foi digitado na variável nome.

    if nome.lower() == "sair":  # Verifica se o usuário digitou "sair".
        break  # Se digitou "sair", interrompe o while e encerra a entrada de nomes.

    convidados.add(nome)  # Se não digitou "sair", adiciona o nome ao conjunto de convidados. Como é um set, nomes repetidos não serão adicionados novamente.

print(f"Convidados confirmados: {', '.join(convidados)}")
# Exibe os convidados confirmados.
# A f-string permite colocar o resultado dentro do texto.
# O join() junta todos os nomes em uma única string,
# colocando ", " entre cada convidado.
