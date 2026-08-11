# Lucas é voluntário na organização de uma maratona e recebeu a lista de participantes com suas respectivas idades. 
# Agora, ele precisa de um programa que apresente três informações:

# Os nomes de todos os participantes.

# As idades de todos os participantes.

# Uma relação completa com o nome e a idade de cada um.

# Sua tarefa é criar esse programa com base nas informações fornecidas.

participantes = {
    "Mariana": 25,
    "Carlos": 32,
    "Beatriz": 28,
    "Rafael": 35
}
# Cria um dicionário onde:
# a chave é o nome do participante
# e o valor é a idade.


print(f"Nomes dos participantes: {', '.join(participantes.keys())}")
# .keys() pega todas as CHAVES do dicionário, ou seja, todos os nomes.
# .join() junta esses nomes em uma única string, separando-os por ", ".
# O print() exibe os nomes.


print(f"Idades dos participantes: {', '.join(str(idade) for idade in participantes.values())}")
# .values() pega todos os VALORES do dicionário, ou seja, todas as idades.
# Como as idades são números (int), precisamos transformá-las em texto
# usando str() antes de utilizar o join().
# Depois, o join() junta todas as idades, separando-as por ", ".


print("Participantes e suas idades:")
# Exibe um título antes de mostrar cada participante com sua idade.


for nome, idade in participantes.items():
    # .items() pega a CHAVE e o VALOR juntos.
    # Nesse caso:
    # nome recebe a chave
    # idade recebe o valor.
    # O for passa por cada participante do dicionário.


    print(f"- {nome}: {idade} anos")
    # Exibe o nome e a idade de cada participante.
