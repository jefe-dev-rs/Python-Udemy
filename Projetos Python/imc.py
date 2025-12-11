# Desafio Calculo de IMC

'''
Criar um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa.
O usuário deve fornecer o peso (em kg) e a altura (em metros).
O programa deve calcular o IMC usando a fórmula: IMC = peso / (altura * altura)
E então, deve classificar o IMC de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 24.9: Peso normal
- Entre 25 e 29.9: Sobrepeso
- Entre 30 e 34.9: Obesidade grau 1
- Entre 35 e 39.9: Obesidade grau 2
- Acima de 40: Obesidade grau 3
'''

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura * altura)
print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso normal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
elif 30 <= imc <= 34.9:
    print("Obesidade grau 1")
elif 35 <= imc <= 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")

