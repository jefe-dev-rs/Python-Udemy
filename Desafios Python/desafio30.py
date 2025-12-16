# Crie uma função lambda
# Que aceite dois números e retorne a multiplicação desses números.
# Em seguida, use essa função para calcular a multiplicação de dois números fornecidos pelo usuário e imprima o resultado.

multiplicacao = lambda x, y: x * y

# Testando a função lambda
num1 = float(input("Digite o primeiro número para multiplicação: "))
num2 = float(input("Digite o segundo número para multiplicação: "))

resultado = multiplicacao(num1, num2)

print(f"A multiplicação de {num1} e {num2} é {resultado}.")