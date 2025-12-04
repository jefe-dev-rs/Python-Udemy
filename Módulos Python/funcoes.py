# funcoes.py

def somar():
    print("Esta Função vai somar os valores")

def multiplicar():
    print("Esta Função vai multiplicar os valores")

def find_index(to_find, lst):
    for i, value in enumerate(to_find):
        if value == lst:
            return i
    return -1