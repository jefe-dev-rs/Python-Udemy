# Listas em Python

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

# Manipulando Listas

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']

cidades[3] = 'Porto Alegre' # Trocou Goiania por Porto Alegre

print(cidades)
print(cidades[0])
print(cidades[1])
print(cidades[2])
print(cidades[3])

# Funções para Manipular Listas

cidades.append('Santa Catarina') # Adicionou Santa Catarina no final da Lista Cidades
print(cidades)

cidades.remove('Salvador') # Removeu Salvador da Lista Cidades
print(cidades)

cidades.insert(1, 'Brasília') # Adicionou Brasília na Posição 1 da Lista Cidades
print(cidades)

cidades.pop(0) # Removeu o item que estava na Posição zero
print(cidades)

cidades.sort() # Coloca a Lista em Ordem
print(cidades)

# Concatenando Listas

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

numeros.extend(letras)
print(numeros)

# Lista com sub Lista

itens = [['item1', 'item2'],[ 'item3', 'item4']]

print(itens[0])
print(itens[1])
print(itens[0][1])
print(itens[1][1])