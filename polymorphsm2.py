# Polymorphsm sem herança no Python

class Cachorro:
    def fazer_som(self):
        print("Au Au")

class Gato:
    def fazer_som(self):
        print("Miau Miau")

animais = [Cachorro(), Gato()]
for a in animais:
    a.fazer_som()


# Exemplo 2

class Pessoa1:
    def microfone(self):
        print("Meu nome é João")

class Pessoa2:
    def microfone(self):
        print("Meu nome é Maria")

pessoas = [Pessoa1(), Pessoa2()]
for p in pessoas:
    p.microfone()



    

