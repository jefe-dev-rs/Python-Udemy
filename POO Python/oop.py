# Programação Orientada a Objetos em Python
# Classes e Objetos
# Classes são utilizadas para criar classes e funções podendo reutilizá-las em diferentes partes do código.

nome = 'João'
nome_lower = nome.lower()  #Converte o nome para letras minúsculas
print(nome_lower)


# Definindo uma classe

class Funcionario:
        nome = 'Elena'
        sobrenome = 'Silva'
        data_nascimento = '10/05/1990'

usuario1 = Funcionario()
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)


