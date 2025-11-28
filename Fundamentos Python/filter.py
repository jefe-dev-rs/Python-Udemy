# Função filter()
# A função filter() constrói um iterador a partir daqueles elementos de um iterável para os quais uma função retorna verdadeiro.

valores = [10, 15, 22, 33, 42, 55, 60]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))  # Saída: [22, 33, 42, 55, 60]
print(list(map(remover20, valores)))     # Saída: [False, False, True, True, True, True, True]