class Animal: # Classe base
    def __init__(self, nome, especie, cor): # Construtor
        self.nome = nome # Atributos
        self.especie = especie # Atributos
        self.cor = cor # Atributos
    
    def apresentar(self): # Método
        print(f'Olá, eu sou um {self.especie} chamado {self.nome} e minha cor é {self.cor}.') # Método
    
class Gato(Animal): # Classe derivada
    def miar(self): # Método específico da classe Gato
        print('Miau!') # Método

class Cachorro(Animal): # Classe derivada
    def latir(self): # Método específico da classe Cachorro
        print('Au Au!') # Método

class Elefante(Animal): # Classe derivada
    def trombar(self): # Método específico da classe Elefante
        print('Tromba! Tromba!') # Método


gato1 = Gato('Mingau', 'Siamese', 'branco') # Instância da classe Gato
gato1.apresentar() # Chamada do método apresentar
gato1.miar() # Chamada do método miar
gato2 = Gato('Tom', 'Persa', 'cinza') # Instância da classe Gato
gato2.apresentar() # Chamada do método apresentar

cachorro1 = Cachorro('Rex', 'Pastor Alemão', 'preto e marrom') # Instância da classe Cachorro
cachorro1.apresentar() # Chamada do método apresentar
cachorro1.latir() # Chamada do método latir
cachorro2 = Cachorro('Bolt', 'Labrador', 'amarelo') # Instância da classe Cachorro
cachorro2.apresentar() # Chamada do método apresentar

elefante1 = Elefante('Dumbo', 'Africano', 'cinza') # Instância da classe Elefante
elefante1.apresentar() # Chamada do método apresentar
elefante1.trombar() # Chamada do método trombar
elefante2 = Elefante('Nhonho', 'Indiano', 'marrom') # Instância da classe Elefante
elefante2.apresentar() # Chamada do método apresentar
