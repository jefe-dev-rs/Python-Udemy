nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
altura = input('Digite a sua altura: ') 
fruta_favorita = input('Digite a sua fruta favorita: ')
print(nome)
print(idade)
print(altura)
print(fruta_favorita)


# sem o f-string
# print('Olá, ' + nome + ', você tem ' + idade + ' anos e sua altura é ' + altura + 'm.')

# usando o f-string
# print(f'Olá, {nome}, você tem {idade} anos e sua altura é {altura}m. e a sua fruta favorita é {fruta_favorita}. ')
print(f'Olá {nome}, daqui 5 anos você terá {idade + 5} anos ')