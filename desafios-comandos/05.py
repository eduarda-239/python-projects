# Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas. 
# Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. Sua tarefa é criar um programa que realize essa operação.

equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}
# Cria um conjunto (set) com as tarefas da equipe A.
# Como é um set, tarefas repetidas não serão armazenadas.


equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}
# Cria um conjunto com as tarefas da equipe B.


tarefas_combinadas = equipe_a.union(equipe_b)
# Junta os elementos dos dois conjuntos em um único conjunto.
# O union() faz a união dos conjuntos.
# Se uma tarefa estiver nas duas equipes, ela aparecerá apenas uma vez.


tarefa_remover = input("Tarefa a ser removida: ").lower()
# Pede para o usuário digitar qual tarefa deseja remover.
# .lower() transforma o texto digitado em letras minúsculas
# para facilitar a comparação com as tarefas armazenadas.


if tarefa_remover in tarefas_combinadas:
# Verifica se a tarefa digitada pelo usuário existe
# dentro do conjunto tarefas_combinadas.


    tarefas_combinadas.remove(tarefa_remover)
    # Se a tarefa existir no conjunto, remove essa tarefa.
    # O .remove() elimina o elemento especificado do set.


print(f"Tarefas finais: {tarefas_combinadas}")
# Exibe o conjunto final de tarefas depois da possível remoção.

