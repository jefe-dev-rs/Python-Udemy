# Sistema de Escola

class Escola:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Aluno(Escola):
    def __init__(self, nome, idade, ano):
        super().__init__(nome, idade)
        self.ano = ano

class Professor(Escola):
    def __init__(self, nome, idade, matéria):
        super().__init__(nome, idade)
        self.matéria = matéria

class Assistente(Escola):
    def __init__(self, nome, idade, bloco):
        super().__init__(nome, idade)
        self.bloco = bloco

a1 = Aluno("João", 16, 2)
print(f' Eu sou {a1.nome} e tenho {a1.idade} anos')
p1 = Professor("Dr. Silva", 45, "Matemática")
print(f' Eu sou {p1.nome} e tenho {p1.idade} anos')
as1 = Assistente("Maria", 30, "A")
print(f' Eu sou {as1.nome} e tenho {as1.idade} anos')

a1.apresentar()
p1.apresentar()
as1.apresentar()
