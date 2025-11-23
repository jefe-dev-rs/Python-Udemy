# Dicionários em Python
# Dicionários são estruturas de dados que armazenam pares de chave-valor (key-value).
# Eles são mutáveis e não ordenados (a partir do Python 3.7, a ordem de inserção é mantida).
# Aceita interios, floats, strings e booleans como chaves.
# São representados por chaves {}.

# Looping através de um dicionário

aluno = {
    'nome': 'Ana',
    'idade': 16,
    'curso': 'Matemática',
    'notas': 'A',
    'materias': ['Física', 'Química', 'Biologia'],
    'aprovado': True
}

for x in aluno:
    print(f"{x}: {aluno[x]}")  # Acessando valor da chave usando o loop

print(aluno.get('materias'))  # Acessando valor da chave 'materias' usando get()
print(len(aluno))  # Imprimindo o número de pares chave-valor no dicionário

print(aluno.keys())    # Imprimindo todas as chaves do dicionário
print(aluno.values())  # Imprimindo todos os valores do dicionário
print(aluno.items())   # Imprimindo todos os pares chave-valor do dicionário

