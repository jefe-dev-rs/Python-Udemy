# Polymorphs com Herança no Python

class Personagem:
    def falar(self):
        raise NotImplementedError("Subclasses devem implementar este método")

class Guerreiro:
    def falar(self):
        print("O guerreiro ataca com uma espada!")
    
class Mago:
    def falar(self):
        print("O mago lança um feitiço!")
    
class Arqueiro:
    def falar(self):
        print("O arqueiro dispara uma flecha!")

# Criar Objetos
personagens = [Guerreiro(), Mago(), Arqueiro()]
for p in personagens:
    p.falar()
    
