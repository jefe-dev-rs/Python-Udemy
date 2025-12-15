# Crie uma funão que aceite dois números como entrada
# Retorne a soma desses dois números

def somar_numeros(num1, num2):
    return num1 + num2

# Solicita ao usuário para inserir dois números
try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = somar_numeros(numero1, numero2)
    print(f"A soma de {numero1} e {numero2} é {resultado}.")
except ValueError:
    print("Por favor, insira números válidos.")
