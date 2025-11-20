"""num1 = 10
num2 = 11

print(num1 == num2) #igual
print(num1 != num2) #diferente
print(num1 > num2) #maior
print(num1 < num2) #menor
print(num1 >= num2) #maior ou igual
print(num1 <= num2) #menor ou igual
print(num1 == 10 and num2 == 11) #e
print(num1 == 10 or num2 == 10) #ou
print(not(num1 == 10)) #não """


# Para dirigir tem que ser maior de idade e ter carteira de habilitação
idade = int(input('Digite a sua idade: ')) 
carteira = input('Você possui carteira de habilitação? (s/n) ')
verificador = idade >= 18 and carteira == 's'
print(f'Sua idade é: {verificador} e você pode dirigir' if verificador else 'Você não pode dirigir')


usuario = input('Digite o nome do usuário: ')
senha = input('Digite a senha: ')
verificador2 = usuario == 'admin' and senha == '12345'
print('Acesso permitido' if verificador2 else 'Acesso negado')