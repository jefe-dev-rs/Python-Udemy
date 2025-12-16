# Crie uma função lambda que aceite um número e retoene se ele é par ou ímpar.
# Em seguida, use essa função para verificar se um número fornecido pelo usuário é par ou ímpar e imprima o resultado.

par_ou_impar = lambda n: "Par" if n % 2 == 0 else "Ímpar"

# Testando a função lambda
user_input = int(input("Digite um número para verificar se é par ou ímpar: "))

resultado = par_ou_impar(user_input)

print(f"O número {user_input} é {resultado}.")

