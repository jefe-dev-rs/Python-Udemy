# Crie uma função lambda que aceite um número e retorne o cubo desse número.
# Em seguida, use essa função para calcular o cubo de um número fornecido pelo usuário e imprima o resultado.

cubo = lambda n: n ** 3

# Testando a função lambda
user_input = int(input("Digite um número para calcular o cubo: "))
resultado = cubo(user_input)
print(f"O cubo de {user_input} é {resultado}.")