# Desafio de funções recursivas: Calcular o fatorial de um número

def fatorial(n):
    """Calcula o fatorial de um número n de forma recursiva."""
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
# Testando a função
user_input = int(input("Digite um número para calcular o fatorial: "))
try:
    resultado = fatorial(user_input)
    print(f"O fatorial de {user_input} é {resultado}.")
except ValueError as e:
    print(e)