# Funções em Python

def saudacao(nome): # Define uma função que recebe um nome como parâmetro
    print(f'Olá {nome}! Bem-vindo ao curso de Python!') # Imprime uma saudação personalizada

saudacao('João') # Chama a função com o nome 'João'
saudacao('Maria') # Chama a função com o nome 'Maria'
saudacao('Pedro') # Chama a função com o nome 'Pedro'

def soma(a, b): # Define uma função que recebe dois números como parâmetros
    return a + b # Retorna a soma dos dois números
resultado = soma(5, 3) # Chama a função soma com os números 5 e 3
print(f'A soma de 5 e 3 é {resultado}') # Imprime o resultado

def multiplica(a, b): # Define uma função que recebe dois números como parâmetros
    return a * b # Retorna o produto dos dois números
resultado = multiplica(4, 2) # Chama a função multiplica com os números 4 e 2
print(f'O produto de 4 e 2 é {resultado}') # Imprime o resultado

def potencia(base, expoente): # Define uma função que recebe uma base e um expoente como parâmetros
    return base ** expoente # Retorna a base elevada ao expoente
resultado = potencia(2, 3) # Chama a função potencia com base 2 e expoente 3
print(f'2 elevado a 3 é {resultado}') # Imprime o resultado

def calcular_desconto(preco, porcentagem): # Define uma função que calcula o preço com desconto
    desconto = preco * (porcentagem / 100) # Calcula o valor do desconto
    return preco - desconto # Retorna o preço com desconto
preco_com_desconto = calcular_desconto(100, 15) # Chama a função com preço 100 e desconto 15%
print(f'O preço com desconto é {preco_com_desconto:.0f}') # Imprime o preço com desconto





