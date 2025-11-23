# Arrays = Matrizes
# Em Python, arrays podem ser implementados usando listas ou a biblioteca array.

from array import array

letras = ['a', 'b', 'c', 'd']  # Lista de caracteres
numeros_i = [1, 2, 3, 4]      # Lista de inteiros
numeros_f = [1.1, 2.2, 3.3]  # Lista de floats

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd'])  # Array de caracteres
numeros_i = array('i', [1, 2, 3, 4])      # Array de inteiros
numeros_f = array('f', [1.1, 2.2, 3.3])  # Array de floats

print(letras)
print(numeros_i)
print(numeros_f)
print()


