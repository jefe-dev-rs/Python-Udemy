# ERROS EM PYTHON
# ERROS SÃO BONS PARA TESTES
# MENSAGENS CUSTOMIZADAS DE ERROS
# Existem vários tipos de erros em Python

try:
    valor = int(input('Digite um número: '))
    print(f'Você digitou o número {valor}')
except ValueError:
    print('Valor inválido! Por favor, digite um número inteiro.')