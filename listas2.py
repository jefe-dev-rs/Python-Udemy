# Extraindo variáveis de Listas

produtos = ['arroz', 'feijão','laranja', 'banana', 4, 5, 6, 8]

item1, item2, item3, *outros = produtos

print(item1)
print(item2)
print(item3)
print(outros)

# Looping dentro de uma Lista

valores = [50, 70, 110, 130, 170]

for x in valores:
    print(f'O valor final do produto é de R${x}')

# Lista de Cores

'''cor_cliente = input('Digite a cor desejada: az')
cores = ['vermelho', 'azul', 'amarelo', 'verde']

if cor_cliente.lower() in cores: # Esta função lower aceita input maisculo ou minusculo
    print('Sim')
else:
    print('Não')'''

# Armazenando mais de uma informação em variáveis

cores = ['vermelho', 'azul', 'amarelo', 'verde']
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores) # o ZIP junta duas listas e deixa os itens de mesmo index juntos

print(list(duas_listas))

# Input em uma Lista

frutas_usuario = input('Digite o nome das frutas separados por virgula: ')

frutas_lista = frutas_usuario.split(', ')
print(frutas_usuario)