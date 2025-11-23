# Lambda functions in Python
# Funções anônimas, ou seja, funções sem nome
# Usadas para criar funções pequenas e simples de forma rápida
# Sintaxe: lambda argumentos: expressão

def somar(x):
    return x + 10
print(somar(5))  # Saída: 15

# Usando lambda para a mesma função
somar_lambda = lambda x: x + 10
print(somar_lambda(2))  # Saída: 12

# Função que usa lambda internamente
def somar2(x): 
    function = lambda x: x + 10
    return function(x) * 4

print(somar2(2))  # Saída: 48