# Função map()
# A função map() aplica uma função a todos os itens de um iterável (como uma lista ou tupla) e retorna um mapa objeto (um iterador) com os resultados.

# Função map em uma lista
numeros = [1, 2, 3, 4, 5]

# Função que será aplicada a cada item
def multi(x):
    return x * 2

# Usando map para aplicar a função multi a cada item da lista numeros
resultado = map(multi, numeros)
print(list(resultado))  # Saída: [2, 4, 6, 8, 10]


# Funão map com lambda
lista2 = [1, 2, 3, 4, 5]

# Usando map com uma função lambda para elevar cada número ao quadrado
resultado_lambda = map(lambda x: x * 2, lista2)
print(list(resultado_lambda))  # Saída: [2, 4, 6, 8, 10]