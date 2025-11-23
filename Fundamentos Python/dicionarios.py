# Dicionários em Python
# Dicionários são estruturas de dados que armazenam pares de chave-valor (key-value).
# Eles são mutáveis e não ordenados (a partir do Python 3.7, a ordem de inserção é mantida).
# Aceita interios, floats, strings e booleans como chaves.
# São representados por chaves {}.

# Criando um dicionário

aluno = {
    'nome': 'Ana',
    'idade': 16,
    'curso': 'Matemática',
    'notas': 'A',
    'aprovado': True
}

aluno['nome'] = 'José'  # Atualizando valor da chave 'nome'
aluno['idade'] += 1     # Incrementando valor da chave 'idade' em 1

aluno.update({'curso': 'Física', 'notas': 'A+'})  # Atualizando múltiplas chaves
aluno.update({'endereço': 'Rua das Flores, 123'})  # Adicionando nova chave-valor
del aluno['aprovado']  # Removendo a chave 'aprovado'
print(aluno)
print(aluno['nome'])  # Acessando valor da chave 'nome'