# ERROS EM PYTHON
# ERROS SÃO BONS PARA TESTES
# MENSAGENS CUSTOMIZADAS DE ERROS
# Existem vários tipos de erros em Python

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print(f'Index não existe!')

