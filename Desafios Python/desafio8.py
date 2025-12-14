# Usar a mesma lista de frutas do desafio anterior
# Seu desafio é alterar a frunta de indice 1 (Banana) para "Morango"
# Depois adicione 'Abacaxi" no final da lista

frutas = ["Maçã", "Banana", "Manga", "Uva"]

frutas[1] = "Morango"          # Alterando o item de índice 1
frutas.append("Abacaxi")      # Adicionando "Abacaxi" no final da lista

print(frutas)                 # Imprimindo a lista atualizada

# Solução alternativa:
# frutas.remove("Banana")
# frutas.append("Morango")
# frutas.append("Abacaxi")
# print(frutas)
