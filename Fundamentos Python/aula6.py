# Exemplo de estrutura condicional simples

numero = int(input("Digite um número: ")) # entrada de dados

if numero == 10: # comparação
    print("Acertou o número 10 ") #se for verdadeiro
else:
    print("Errou, o número é diferente de 10") # se for falso


# Exemplo de estrutura condicional composta

idade = int(input("Qual é a sua idade: ")) # entrada de dados

if idade >= 18: # comparação
    print("Você é maior de idade") # se for verdadeiro
else:
    print("Você é menor de idade") # se for falso

# Aula - Estruturas Condicionais

nota_aluno = float(input("Qual foi sua nota: "))

if nota_aluno >= 7.0:
    print("Parabéns, você foi aprovado!")
elif 5.0 <= nota_aluno < 7.0:
    print("Você está de recuperação, estude mais!")
else:
    print("Você foi reprovado, estude mais da próxima vez!")



