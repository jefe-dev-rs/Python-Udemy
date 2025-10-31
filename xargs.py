# Função com vários Argumentos
""""
def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2, 3, 4, 7)

print(x)
"""

# Criar uma função que Armazena Números e Strings (Dados)

def agencia(**carro):
    return carro


print(agencia(marca = 'Gol', cor = 'Branca', motor =  1.0))
print(agencia(marca = 'Corsa', cor = 'Cinza', motor =  1.6))
print(agencia(Prisma = 'Gol', cor = 'Prata', motor =  1.4))