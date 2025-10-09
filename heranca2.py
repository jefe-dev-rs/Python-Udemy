class Pessoa: # Superclasse
    def __init__(self, nome, idade): # Construtor
        self.nome = nome # Atributo
        self.idade = idade # Atributo

    def apresentar(self): # Método
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.") # Fala o nome e a idade

class Funcionario(Pessoa): # Subclasse
    def __init__(self, nome, idade, cargo): # Construtor
        super().__init__(nome, idade) # Chama o construtor da superclasse
        self.cargo = cargo # Atributo
    def trabalhar(self): # Método
        print(f"{self.nome} está trabalhando como {self.cargo}.") # Fala o nome e o cargo

class Cliente(Pessoa): # Subclasse
    def __init__(self, nome, idade, saldo): # Construtor
        super().__init__(nome, idade) # Chama o construtor da superclasse
        self.saldo = saldo # Atributo

    def comprar(self, valor_compra): # Método
        if valor_compra <= self.saldo: # Verifica se o saldo é suficiente
            self.saldo -= valor_compra # Deduz o valor da compra do saldo
            print(f"{self.nome} comprou um item por {valor_compra}. Saldo restante: {self.saldo}.") # Fala o nome, o valor da compra e o saldo restante
        else: # Se o saldo não for suficiente
            print(f"{self.nome} não tem saldo suficiente para comprar este item.") # Fala que não tem saldo suficiente

f1 = Funcionario('Ana', 28, 'Dev Junior ') # Instância da classe Funcionario
f1.trabalhar() # Chama o método trabalhar
#c1 = Cliente('Carlos', 35)
#c1.apresentar()
c1 = Cliente('Carlos', 35, 200) # Instância da classe Cliente
c1.comprar(30) # Chama o método comprar
c2 = Cliente('Beatriz', 22, 100) # Instância da classe Cliente
c2.comprar(150) # Chama o método comprar