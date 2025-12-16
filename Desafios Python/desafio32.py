# Crie uma função lambda que eleve o número ao quadrado.
# Em seguida , use essa função para calcular o quadrado de um número fornecido em um for loop de 1 a 10 e imprima o resultado.

quadrado = lambda n: n ** 2

# Testando a função lambda em um loop de 1 a 10
for i in range(1, 11):
    resultado = quadrado(i)
    print(f"O quadrado de {i} é {resultado}.")
