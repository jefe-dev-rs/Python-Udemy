from datetime import datetime
# Classe

class Funcionario:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        return ano_atual - self.ano_nascimento
    
# Criando objetos da classe Funcionario usando o construtor
funcionario1 = Funcionario('Carlos', 'Santos', 1985)
funcionario2 = Funcionario('Ana', 'Oliveira', 1990)
funcionario3 = Funcionario('Marcos', 'Pereira', 1980)

# Printando os valores dos parâmetros do objeto funcionario1
print(funcionario1.nome_completo())
print(f"Idade: {funcionario1.idade_funcionario()} anos")
print(funcionario2.nome_completo())
print(f"Idade: {funcionario2.idade_funcionario()} anos")
print(funcionario3.nome_completo())
print(f"Idade: {funcionario3.idade_funcionario()} anos")