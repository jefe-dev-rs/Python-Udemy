# Desafio do if, else e elif

'''
Criar um programa em que dependendo a temperatura do steak (bife) ele retorne se o ponto do bife é mal passado, ao ponto ou bem passado.

- 120°F = 49°C - Rare (Mal passado)
- 130°F = 54°C - Medium Rare (Ao ponto para mal passado)
- 140°F = 60°C - Medium (Ao ponto)
- 150°F = 65°C - Medium Well (Ao ponto para bem passado)
- 160°F = 71°C - Well Done (Bem passado)
'''

tem_celcius = float(input("Digite a temperatura do bife em Celsius: "))

if tem_celcius < 48:
    print('Cozinhar por mais alguns minutos!')
elif tem_celcius in range(48, 53):
    print('O bife está mal passado.')
elif tem_celcius in range(54, 59):
    print('O bife está ao ponto.')
elif tem_celcius in range(60, 65):
    print('O bife está ao ponto para bem passado.')
elif tem_celcius in range(66, 70):
    print('O bife está bem passado.')
else:
    print('Está Queimada!')