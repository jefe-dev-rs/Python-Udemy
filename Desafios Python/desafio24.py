# Crie uma funão que aceite um número e retone o quadrado desse número

def calcular_quadrado(numero):
    return numero ** 2

# Solicita ao usuário para inserir um número
try:
    numero_usuario = float(input("Digite um número para calcular o quadrado: "))
    resultado = calcular_quadrado(numero_usuario)
    print(f"O quadrado de {numero_usuario} é {resultado}.")
except ValueError:
    print("Por favor, insira um número válido.")

