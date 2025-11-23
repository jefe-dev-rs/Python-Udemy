# Tuplas

'''
Armazenar múltiplos valores em uma única variável.
Não podem ser alteradas (imutáveis).
São representadas por parênteses ().
'''
cores_list = ['vermelho', 'verde', 'azul']  # Lista (mutável)
cores_tuple = ('vermelho', 'verde', 'azul')  # Tupla (imutável)

print(type(cores_list))  # <class 'list'>
print(cores_list)
print(type(cores_tuple))  # <class 'tuple'>
print(cores_tuple)

duas_list = cores_list * 2
duas_tuple = cores_tuple * 2
print(duas_list)   # ['vermelho', 'verde', 'azul', 'vermelho', 'verde', 'azul']
print(duas_tuple)  # ('vermelho', 'verde', 'azul', 'vermelho', 'verde', 'azul')
print(len(cores_list))   # 3
print(len(cores_tuple))  # 3