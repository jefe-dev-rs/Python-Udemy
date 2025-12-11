# Desafio de Sets

'''
Criar um programa que gere 3 listas de acordo com os critérios abaixo:
Lista1: Funcionários que tem carro e trabalham a noite.
Lista2: Funcionários que tem carro e trabalham de dia.
Lista3: Funcionários que não tem carro.
'''

funcionarios = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo', 'Fernanda', 'Gustavo ']
turno_dia = ['Ana', 'Daniel', 'Fernanda', 'Gustavo ']
turno_noite = ['Bruno', 'Carla', 'Eduardo']
tem_carro = ['Ana', 'Bruno', 'Carla', 'Eduardo']

# Lista1
lista1 = set(tem_carro).intersection(set(turno_noite))
print("Funcionários que tem carro e trabalham a noite:", lista1)

# Lista2
lista2 = set(tem_carro).intersection(set(turno_dia))
print("Funcionários que tem carro e trabalham de dia:", lista2)

# Lista3
lista3 = set(funcionarios).difference(set(tem_carro))
print("Funcionários que não tem carro:", lista3)
