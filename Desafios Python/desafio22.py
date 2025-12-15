# Crie uma Lista com 5 Nomes de Países e suas Capitais
# Peça ao usuário para digitar o nome de um país
# Se o país estiver na lista, imprima "A capital de [país] é [capital]!"
# Caso contrário, imprima "País [país] não encontrado."

paises_capitais = { # Dicionário de países e suas capitais
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "Colômbia": "Bogotá",
    "Chile": "Santiago",
    "Peru": "Lima"
}  

pais_usuario = input("Digite o nome de um país: ")
pais_usuario_formatado = pais_usuario.title()  # Formata a entrada do usuário para corresponder às chaves do dicionário

if pais_usuario_formatado in paises_capitais:
    capital = paises_capitais[pais_usuario_formatado]
    print(f"A capital de {pais_usuario_formatado} é {capital}!")
else:
    print(f"País {pais_usuario} não encontrado.")