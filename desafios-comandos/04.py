# Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões faz parte das permissões principais de um sistema. 
# Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.


permissoes_principais = set(
    p.strip() for p in input("Permissões principais: ").lower().split(',')
)
# Pede para o usuário digitar as permissões principais.
# .lower() transforma tudo em letras minúsculas.
# .split(',') separa as permissões sempre que encontra uma vírgula.
# p.strip() remove espaços extras antes ou depois de cada permissão.
# set() transforma tudo em um conjunto e elimina possíveis repetições.


permissoes_solicitadas = set(
    p.strip() for p in input("Permissões solicitadas: ").lower().split(',')
)
# Faz a mesma coisa com as permissões solicitadas.


eh_subconjunto = permissoes_solicitadas.issubset(permissoes_principais)
# Verifica se TODAS as permissões solicitadas estão dentro
# das permissões principais.
# .issubset() retorna True se estiverem todas presentes
# e False se pelo menos uma não estiver.


if eh_subconjunto:
    # Se eh_subconjunto for True, executa o código abaixo.

    print("As permissões solicitadas fazem parte das permissões principais.")
    # Mostra a mensagem informando que todas as permissões solicitadas
    # estão presentes nas permissões principais.

else:
    # Se eh_subconjunto for False, executa o código abaixo.

    print("As permissões solicitadas não fazem parte das permissões principais.")
    # Mostra a mensagem informando que nem todas as permissões solicitadas
    # estão presentes nas permissões principais.
