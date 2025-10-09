class Pessoa: # 
    def __init__(self, nome, idade, cargo): # Método construtor
        self.nome = nome # Atributo nome
        self.idade = idade # Atributo idade
        self.cargo = cargo # Atributo cargo

    def informacoes(self): # Método para exibir informações da pessoa
        print(f"Nome: {self.nome}, Idade: {self.idade}, Cargo: {self.cargo}") # Exibe as informações da pessoa

    def promover(self, novo_cargo): # Método para promover a pessoa
        self.cargo = novo_cargo # Atualiza o cargo da pessoa
        print(f"{self.nome} foi promovido(a) para {self.cargo}.") # Mensagem de confirmação

    def atualizar_idade(self, nova_idade): # Método para atualizar a idade da pessoa
        if nova_idade > self.idade: # Verifica se a nova idade é maior que a atual
            self.idade = nova_idade # Atualiza a idade
            print(f"A idade de {self.nome} foi atualizada para {self.idade}.") # Mensagem de confirmação
        else:   # Se a nova idade não for maior que a atualself.idade = nova_idade
            print(f"A idade de {self.nome} foi atualizada para {self.idade}.")
            print("A nova idade deve ser maior que a atual.") # Mensagem de erro

# Instantiate objects and call methods outside the class definition
colaborador1 = Pessoa("Ana", 30, "Desenvolvedora")
colaborador2 = Pessoa("Bruno", 25, "Designer")
    
colaborador1.informacoes() # Exibe as informações do colaborador
colaborador1.promover("Líder de Equipe") # Promove o colaborador
colaborador1.atualizar_idade(31) # Atualiza a idade do colaborador
colaborador2.informacoes() # Exibe as informações do colaborador
colaborador2.promover("Senior Designer") # Promove o colaborador
colaborador2.atualizar_idade(27) # Atualiza a idade do colaborador