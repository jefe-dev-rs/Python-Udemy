# Criar um loop que conte de 1 a 10
# Use o Break para parar o loop quando chegar em 5
# Crie um outro loop que conte de 1 a 10
# Use o Continue para pular o número 5

# Primeiro loop com Break
for numero in range(1, 11):
    if numero > 5:
        break
    print(numero)
print("Loop com Break finalizado.")

# Segundo loop com Continue
for numero in range(1, 11):
    if numero == 5:
        continue
    print(numero)
print("Loop com Continue finalizado.")

