# Herança Multipla e Herança de Multinivel
# Classe Avô -> Classe Pai -> Classe Filho
class Animal: # Classe avô
    def __init__(self, nome): # Método construtor
        self.nome = nome # Atributo
        
# Classes pai
class Predador(Animal): # Classe pai
    def cacando(self): # Método
        print(f'O animal {self.nome} está Caçando...') # Método

class Presa(Animal): # Classe pai
    def fugindo(self): # Método
        print(f'O animal {self.nome} está Fugindo...') # Método

# Classe filho herdando de múltiplas classes pai

class Coelho(Presa):
    pass
class Tigre(Predador): 
    pass
class Golfinho(Predador, Presa):
    pass

Coelho1 = Coelho('Teo') # Instância
Tigre1 = Tigre('Leo') # Instância
Golfinho1 = Golfinho('Bily') # Instância


Coelho1.fugindo() # Chamando o método da classe pai
Tigre1.cacando() # Chamando o método da classe pai
Golfinho1.cacando() # Chamando o método da classe pai
Golfinho1.fugindo() # Chamando o método da classe pai


