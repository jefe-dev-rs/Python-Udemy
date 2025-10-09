from funcoes import saudacao, soma

saudacao('Jeferson')
resultado = soma(5, 10)
print(f"O resultado da soma é: {resultado}")


from funcoes import verificar_maioridade
minha_idade = int(input("Digite sua idade: "))

if verificar_maioridade(minha_idade):
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
