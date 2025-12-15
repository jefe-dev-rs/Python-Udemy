# Crie uma lista de números de 1 a 10
# Use um for loop para iterar sobre a lista
# Dentro do loop, use um if statement para verificar se o número é par ou ímpar
# Imprima "Número [número] é par" ou "Número [número] é ímpar" conforme apropriado

numeros = list(range(1, 11))
for numero in numeros:
    if numero % 2 == 0:
        print(f"Número {numero} é par")
    else:
        print(f"Número {numero} é ímpar")