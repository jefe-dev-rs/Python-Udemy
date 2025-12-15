# Desafio de loja de carros da BMW
# Crie uma lista de carros disponíveis na loja: BMW X1, BMW X3, BMW X5, BMW M3, BMW M5.
# Peça ao usuário para inserir o modelo do carro que deseja comprar.
# Se o modelo estiver na lista, imprima "Parabéns! Você comprou um [modelo do carro]".
# Se o modelo não estiver na lista, imprima "Desculpe, esse modelo não está disponível".

carros_disponiveis = ["BMW X1", "BMW X3", "BMW X5", "BMW M3", "BMW M5"]
modelo_desejado = input("Insira o modelo do carro que deseja comprar: ")

if modelo_desejado in carros_disponiveis:
    print(f"Parabéns! Você comprou um {modelo_desejado}")
else:
    print("Desculpe, esse modelo não está disponível")

