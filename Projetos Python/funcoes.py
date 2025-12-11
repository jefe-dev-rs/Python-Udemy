# Desafio de funções

'''
Criar um programa que calcule a tinta necessária para pintar uma parede.
O usuário deve fornecer a largura e a altura e o rendimento da tinta (em metros quadrados por litro).
'''

rendimento = int(input("Digite o rendimento da tinta (m² por litro): "))
largura = int(input("Digite a largura da parede (em metros): "))
altura = int(input("Digite a altura da parede (em metros): "))

def calcular_tinta(rendimento, largura, altura):
    area = largura * altura
    tinta_necessaria = area / rendimento
    print(f'Serão necessários {tinta_necessaria:.2f} litros de tinta para pintar a parede.')

calcular_tinta(rendimento, largura, altura)