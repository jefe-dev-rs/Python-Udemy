# Crie uma lista de frutas que inclua maçã 3 vezes.
# Use um loop para contar quantas vezes a maçã aparece na lista.

frutas = ["maçã", "banana", "cereja", "maçã", "laranja", "maçã"]

contador_maca = 0

for fruta in frutas:
    if fruta == "maçã":
        contador_maca += 1
print(f"A maçã aparece {contador_maca} vezes na lista.")

