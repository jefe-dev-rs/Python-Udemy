# Programação Orientada a Objetos em Python

class Casa: # Definição da classe Casa
    def __init__(self, cor, quartos, banheiros): # Método construtor
        self.cor = cor # Atributo cor
        self.quartos = quartos # Atributo quartos
        self.banheiros = banheiros # Atributo banheiros
    def mostrar_cor(self): # Método para mostrar a cor da casa
        print(f"A cor da casa é {self.cor}")  # F-String para formatação
    def mostrar_quartos(self): # Método para mostrar o número de quartos
        print(f"A casa tem {self.quartos} quartos") # F-String para formatação
    def mostrar_banheiros(self): # Método para mostrar o número de banheiros
        print(f"A casa tem {self.banheiros} banheiros") # F-String para formatação
    def adicionar_quarto(self): # Método para adicionar um quarto
        self.quartos += 1 # Incrementa o número de quartos
        print(f'Um quarto foi adicionado. Agora a casa tem {self.quartos} quartos.') # F-String para formatação
    def pintar(self, nova_cor): # Método para pintar a casa
        print(f'A casa foi pintada de {self.cor} para {nova_cor}.') # F-String para formatação


casa1 = Casa("azul",4,2) # Instância da classe Casa
casa2 = Casa("vermelha",6,3) # Instância da classe Casa

print('\ncasa1: ') # Exibindo informações da casa1
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()
casa1.pintar('laranja')

print('\ncasa2: ') # Exibindo informações da casa2
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.adicionar_quarto()