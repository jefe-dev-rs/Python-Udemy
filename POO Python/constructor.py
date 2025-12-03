# Construtores in Python
# Construtores são métodos especiais usados para inicializar objetos de uma classe.

class Funcionario:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

# Criando objetos da classe Funcionario usando o construtor
funcionario1 = Funcionario('Carlos', 'Santos', '15/08/1985')
funcionario2 = Funcionario('Ana', 'Oliveira', '22/11/1990')
funcionario3 = Funcionario('Marcos', 'Pereira', '30/03/1980')

# Printando os valores dos parâmetros do objeto funcionario1
print(funcionario1.nome)
print(funcionario1.sobrenome)
print(funcionario1.data_nascimento)

# Printando os valores dos parâmetros do objeto funcionario2
print(funcionario2.nome)
print(funcionario2.sobrenome)
print(funcionario2.data_nascimento)

# Printando os valores dos parâmetros do objeto funcionario3
print(funcionario3.nome)
print(funcionario3.sobrenome)
print(funcionario3.data_nascimento)
