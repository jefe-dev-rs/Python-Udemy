# Crie uma lista de 3 Cidades do Brasil
# Peça ao usuário para digitar o nome de uma cidade
# Se a cidade estiver na lista, imprima "Cidade [cidade] encontrada!"
# Caso contrário, imprima "Cidade [cidade] não encontrada."
# Não pode utilizar o list[]

cidades = ("São Paulo", "Rio de Janeiro", "Belo Horizonte") # Tupla de cidades

cidade_usuario = input("Digite o nome de uma cidade: ")

if cidade_usuario.lower() in map(str.lower, cidades): # Verifica se a cidade está na tupla, ignorando maiúsculas/minúsculas
    print(f"Cidade {cidade_usuario} encontrada!")
else:
    print(f"Cidade {cidade_usuario} não encontrada.")
