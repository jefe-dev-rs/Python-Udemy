# Desafio de Potência de um Número
# A função deve aceitar dois números: a base e o expoente
# Retorne a base elevada ao expoente
# Se o expoente não for fornecido, ele deve ser considerado como 2 (quadrado)

def potencia(base, expoente=2):
    return base ** expoente

# Solicita ao usuário para inserir a base e o expoente
try:
    base_usuario = float(input("Digite a base (número): "))
    expoente_usuario_input = input("Digite o expoente (pressione Enter para usar o valor padrão 2): ")
    
    if expoente_usuario_input.strip() == "":
        resultado = potencia(base_usuario)
    else:
        expoente_usuario = float(expoente_usuario_input)
        resultado = potencia(base_usuario, expoente_usuario)
    
    print(f"{base_usuario} elevado a {expoente_usuario_input if expoente_usuario_input.strip() != '' else 2} é {resultado}.")
except ValueError:
    print("Por favor, insira números válidos.")
