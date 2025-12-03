# Classes

class Funcionario:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

# Criando objetos da classe Funcionario usando o construtor
funcionario1 = Funcionario('Carlos', 'Santos', '15/08/1985')
funcionario2 = Funcionario('Ana', 'Oliveira', '22/11/1990')
funcionario3 = Funcionario('Marcos', 'Pereira', '30/03/1980')

# Printando os valores dos parâmetros do objeto funcionario1
print(funcionario1.nome_completo())
print(funcionario2.nome_completo())
print(funcionario3.nome_completo())