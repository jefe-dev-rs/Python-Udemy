# Dicionários em Python
# Um dicionário é uma coleção de pares chave-valor.
# Cada chave é única e é usada para acessar o valor associado a ela.
# Dicionários são mutáveis, o que significa que podemos alterar, adicionar ou remover itens.
# Criando um dicionário

usuario = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}
print(usuario) # Imprimindo o dicionário completo
print(usuario["nome"])  # Acessando valor pela chave
print(usuario.get("idade"))  # Outra forma de acessar valor pela chave

usuario["idade"] = 31  # Atualizando valor
usuario["email"] = "jefe@gmail.com" # Adicionando novo par chave-valor
print(usuario)
del usuario["cidade"]  # Removendo par chave-valor
print(usuario)
# Iterando sobre um dicionário
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")
# Verificando se uma chave existe
if "nome" in usuario:
    print("A chave 'nome' existe no dicionário.")
# Obtendo todas as chaves
chaves = usuario.keys()
print(chaves)
# Obtendo todos os valores
valores = usuario.values()
print(valores)
# Limpando o dicionário
usuario.clear()
print(usuario) # Imprimindo o dicionário após limpar
# Deletando o dicionário
del usuario
# print(usuario) # Isso causará um erro, pois o dicionário foi deletado
# Fim do código