# Desafio de criar um loop
# Peça ao usuário para inserir o nome de uma fruta
# Continue o loop até o usuário acertar a fruta "abacate"

fruta_correta = "abacate"
fruta_usuario = ""

while fruta_usuario.lower() != fruta_correta:
    fruta_usuario = input("Insira o nome de uma fruta: ")
    if fruta_usuario.lower() != fruta_correta:
        print("Tente novamente!")
print("Parabéns! Você acertou a fruta.")



