# List Comprehension
# Uma forma concisa de criar listas
# Sintaxe: [expressão for item in iterável if condição]

'''frutas1 = ['maçã', 'banana', 'laranja', 'abacaxi', 'uva']
frutas2 = []

for itens in frutas1:
    if 'b' in itens:
        frutas2.append(itens)

print(frutas2)  # Saída: ['banana', 'abacaxi']'''


# Usando List Comprehension para filtrar frutas com a letra 'b'
frutas1 = ['maçã', 'banana', 'laranja', 'abacaxi', 'uva']
frutas2 = [itens for itens in frutas1 if 'b' in itens]
print(frutas2)  # Saída: ['banana', 'abacaxi']

# Usando List Comprehension com números
valores = []
'''
for x in range(6):
    valores.append(x * 10)
print(valores)  # Saída: [0, 10, 20, 30, 40, 50]
'''
valores = [x * 10 for x in range(6)]
print(valores)  # Saída: [0, 10, 20, 30, 40, 50]