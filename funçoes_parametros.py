# Funções com Parâmetros

"""def boas_vindas_Marcos():
    print('Olá Marcos')
    print('Temos 5 Laptops')


def boas_vindas_Ronaldo():
    print('Olá Ronaldo')
    print('Temos 4 Laptops')


def boas_vindas_Linda():
    print('Olá Linda')
    print('Temos 3 Laptops')

boas_vindas_Marcos()
boas_vindas_Ronaldo()
boas_vindas_Linda()"""

def boas_vindas(nome, quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque.')

boas_vindas('Marcos',5)
boas_vindas('Ronaldo',4)
boas_vindas('Linda',3)
