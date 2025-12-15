# DEsafio utilizando o if, else e elif
# Crie um programa que peça que o usuário insira sua idade.
# Se a idade for menor que 13, imprima "Você é uma criança".
# Se a idade for entre 13 e 19 (inclusive), imprima "Você é um adolescente".
# Se a idade for 20 ou mais, imprima "Você é um adulto".

idade = int(input("Insira sua idade: "))

if idade < 13:
    print("Você é uma criança")
elif 13 <= idade <= 19:
    print("Você é um adolescente")
else:
    print("Você é um adulto")

