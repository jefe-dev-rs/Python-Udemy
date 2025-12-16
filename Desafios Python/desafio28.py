# Crie duas funções
# A primeira função deve aceitar um número e retornar o dobro desse número.
# A segunda função deve aceitar um número e retornar o quadrado desse número.
# Em seguida chame a primeira função dentro da segunda função e imprima o resultado.

def dobro(n):
    """Retorna o dobro de um número n."""
    return n * 2

def quadrado(n):
    """Retorna o quadrado do dobro de um número n."""
    return dobro(n) ** 2

# Testando as funções
user_input = int(input("Digite um número para calcular o quadrado do seu dobro: "))
resultado = quadrado(user_input)
print(f"O quadrado do dobro de {user_input} é {resultado}.")

