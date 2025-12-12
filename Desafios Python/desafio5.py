# Desafio de calculos Matemáticos
'''
Solicitar ao usuário dois números
Depois, imprimir a soma, subtração, multiplicação e divisão e exponenciação entre esses dois números.
'''

# Solicitar os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizar os cálculos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
exponenciacao = num1 ** num2

# Imprimir os resultados
print(f"A soma entre {num1} e {num2} é {soma}.")
print(f"A subtração entre {num1} e {num2} é {subtracao}.")
print(f"A multiplicação entre {num1} e {num2} é {multiplicacao}.")
print(f"A divisão entre {num1} e {num2} é {divisao}.")
print(f"A exponenciação de {num1} elevado a {num2} é {exponenciacao}.")

