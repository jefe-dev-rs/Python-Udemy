# Crie 2 sets: Cada um contendo 5 nomes de pessoas
# Alguns nomes podem estar repetidos entre os sets
# Use um metodo para verificar os nomes que estão em ambos os sets

set1 = {"Ana", "Bruno", "Carla", "Daniel", "Eduardo"}
set2 = {"Fernanda", "Bruno", "Gabriel", "Ana", "Helena"}

nomes_comuns = set1.intersection(set2) # Verifica os nomes que estão em ambos os sets

if nomes_comuns:
    print("Nomes em ambos os sets:", ", ".join(nomes_comuns))
else:
    print("Não há nomes em comum entre os sets.")
