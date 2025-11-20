# Exemplo de uma classe Carro com atributos e métodos
class Carro: # Definição da classe Carro
    def __init__(self, marca, modelo, ano): # Método construtor
        self.marca = marca # Atributo marca
        self.modelo = modelo # Atributo modelo
        self.ano = ano # Atributo ano
        self.ligado = True # Atributo ligado7
        self.seta = None # Atributo seta

    def informacoes(self): # Método para exibir informações do carro
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}") # Exibe as informações do carro

    def ligar(self): # Método para ligar o carro
        if not self.ligado: # Verifica se o carro está desligado
            self.ligado = True # Liga o carro
            print("O carro foi ligado.") # Mensagem de confirmação
        else: # Se o carro já estiver ligado
            print("O carro já estava ligado.") # Mensagem informando que o carro já está ligado
    def desligar(self): # Método para desligar o carro
        if self.ligado: # Verifica se o carro está ligado
            self.ligado = False # Desliga o carro
            print("O carro foi desligado.") # Mensagem de confirmação
        else: # Se o carro já estiver desligado
            print("O carro já estava desligado.") # Mensagem informando que o carro já está desligado

    def ligar_seta(self, direcao): # Método para ligar a seta
        if direcao in ["esquerda", "direita"]: # Verifica se a direção é válida
            self.seta = direcao # Define a direção da seta
            print(f"A seta foi ligada para a {direcao}.") # Mensagem de confirmação
        else: # Se a direção não for válida
            print("Direção inválida. Use 'esquerda' ou 'direita'.") # Mensagem de erro
    
carro1 = Carro("Toyota", "Corolla", 2020) # Criação de uma instância da classe Carro
carro1.informacoes() # Exibe as informações do carro
carro1.ligar() # Liga o carro
carro1.desligar() # Desliga o carro
carro1.ligar_seta("esquerda") # Liga a seta para a esquerda
carro1.ligar_seta("direita") # Liga a seta para a direita
carro1.ligar_seta("frente") # Tenta ligar a seta com uma direção inválida

