# Criando Sets em Python

'''
São similares às listas e tuplas, mas com algumas diferenças importantes:
- Não permitem elementos duplicados.
- Não possuem ordem definida (não são indexados).
- São mutáveis, ou seja, você pode adicionar ou remover elementos.
'''
# Criando um set

list1 = [10, 20, 30, 40, 50]
s1 = {10, 20, 30, 40, 50}
s1.add(60)  # Adicionando um elemento ao set
s1.update([70, 80, 90])  # Adicionando múltiplos elementos ao set
s1.remove(20)  # Removendo um elemento do set
s1.discard(100)  # Removendo um elemento que não existe (não gera erro)
list1.append(60)  # Adicionando um elemento à lista


print(list1)
print(s1)
print(type(list1))  # <class 'list'>
print(type(s1))     # <class 'set'>