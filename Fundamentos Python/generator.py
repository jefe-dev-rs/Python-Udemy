# Generator Expression
# Uma forma concisa de criar geradores em Python usando uma sintaxe semelhante à de listas.
# Sintaxe: (expressão for item in iterável if condição)

from sys import getsizeof  # <--- A linha que faltava!

# --- LISTA (Gasta mais memória) ---
numeros = [x * 10 for x in range(10)]
print(type(numeros))
print(numeros)
print(f"Tamanho da Lista na memória: {getsizeof(numeros)} bytes")

print("-" * 30)

# --- GERADOR (Gasta menos memória) ---
numeros2 = (x * 10 for x in range(10))
print(type(numeros2))
print(f"Tamanho do Gerador na memória: {getsizeof(numeros2)} bytes")

# CUIDADO: Ao fazer o print abaixo, você "esvazia" o gerador!
print(list(numeros2))  # Converte o gerador em uma lista para exibir os valores