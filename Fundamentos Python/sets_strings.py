# Criando Sets em Python

'''
São similares às listas e tuplas, mas com algumas diferenças importantes:
- Não permitem elementos duplicados.
- Não possuem ordem definida (não são indexados).
- São mutáveis, ou seja, você pode adicionar ou remover elementos.
'''
# Criando um set

set1 = {'a', 'b', 'c', 'd'}  # Criando um set com elementos
set2 = {'a', 'b', 'a', 'c', 'd', 'b'}  # Elementos duplicados serão ignorados
set3 = {'a', 1, 2.5, True}  # Set com tipos de dados mistos

set4 = set1.union(set3)  # União de dois sets
set4 = set1.difference(set3)  # Diferença entre dois sets
set4 = set1.intersection(set2)  # Interseção entre dois sets
print(set4)