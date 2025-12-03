# Programação Orientada a Objetos em Python
# Classes e Objetos
# Classes são utilizadas para criar classes e funções podendo reutilizá-las em diferentes partes do código.

# Criando Objetos dentro de uma Classe

# Criar Classe Funcionarios
class Funcionarios:
    pass

# Criar Objetos dentro da Classe Funcionarios
funcionario1 = Funcionarios()
funcionario2 = Funcionarios()


# Criar os parâmetros do usuario 1
funcionario1.nome = 'Carlos'
funcionario1.sobrenome = 'Santos'
funcionario1.data_nascimento = '15/08/1985'

# Criar os parâmetros do usuario 2
funcionario2.nome = 'Ana'
funcionario2.sobrenome = 'Oliveira'
funcionario2.data_nascimento = '22/11/1990'

# Printando os valores dos parâmetros do objeto funcionario1
print(funcionario1.nome)
print(funcionario1.sobrenome)
print(funcionario1.data_nascimento)

# Printando os valores dos parâmetros do objeto funcionario2
print(funcionario2.nome)
print(funcionario2.sobrenome)
print(funcionario2.data_nascimento)