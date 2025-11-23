# Criando Sets em Python

'''
São similares às listas e tuplas, mas com algumas diferenças importantes:
- Não permitem elementos duplicados.
- Não possuem ordem definida (não são indexados).
- São mutáveis, ou seja, você pode adicionar ou remover elementos.
'''
# Criando um set

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 40, 70]

num1 = set(list1)
num2 = set(list2)

print("Set 1:", num1)  # Set 1: {10, 20, 30, 40, 50}
print("Set 2:", num2)  # Set 2: {70, 10, 20, 40}
print()
# Operações com Sets
print(num1 | num2)  # União: {70, 10, 20, 40, 50, 30}
print(num1 & num2)  # Interseção: {10, 20,
print(num1 - num2)  # Diferença: {50, 30}
print(num1 ^ num2)  # Diferença simétrica: {70, 50, 30}

