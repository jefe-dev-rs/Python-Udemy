# Utilize a lista de frutas do desafio anterior e imprima cada fruta em uma linha diferente na tela.
# Remova a fruta "Manga" com o metodo remove() e imprima a lista atualizada.
# Remova o ultimo item da lista usando o comando del e imprima a lista atualizada.

frutas = ["Maçã", "Morango", "Manga", "Abacaxi", "Uva"]

for fruta in frutas:
    print(fruta)

frutas.remove("Manga") # Remove a fruta "Manga"
print(frutas)

del frutas[-1] # Remove o último item da lista
print(frutas)