# Use o "For loop" aninhado
# Crie um loop com frutas e vegetais
# As frutas primeiros e depois os vegetais

frutas = ["maçã", "banana", "cereja"]
vegetais = ["cenoura", "batata", "alface"]

for fruta in frutas:
    print(f"Fruta: {fruta}")
    for vegetal in vegetais:
        print(f"  Vegetal: {vegetal}")