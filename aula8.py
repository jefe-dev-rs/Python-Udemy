# Exemplos de uso de listas em Python

frutas = ['maçã', 'banana', 'laranja']
print(frutas)  # Imprime a lista completa
print(frutas[0])  # Imprime o primeiro elemento da lista
print(frutas[-1])  # Imprime o último elemento da lista
print(frutas[1:3])  # Imprime uma fatia da lista (do índice 1 ao 2)

frutas.append('uva')  # Adiciona um elemento ao final da lista
print(frutas)

frutas.remove('banana')  # Remove um elemento da lista
print(frutas)
frutas.insert(1, 'morango')  # Insere um elemento na posição 1
print(frutas)
frutas.pop()  # Remove o último elemento da lista
print(frutas)
frutas.extend(['kiwi', 'abacaxi'])  # Adiciona múltiplos elementos ao final da lista
print(frutas)
frutas.sort(reverse=True)  # Ordena a lista em ordem decrescente
print(frutas)
frutas.sort()  # Ordena a lista em ordem alfabética
print(frutas)
frutas.reverse()  # Inverte a ordem da lista
print(frutas)
print(len(frutas))  # Imprime o tamanho da lista
frutas.clear()  # Limpa todos os elementos da lista
print(frutas)

tarefas = [] # Lista para armazenar tarefas

tarefas.append("Estudar Python") # Adiciona uma tarefa à lista
tarefas.append("Fazer exercícios") # Adiciona outra tarefa
tarefas.append("Ler documentação") # Adiciona mais uma tarefa

print('Minhas Tarefas de Hoje: ') # Imprime o título
for tarefa in tarefas: # Itera sobre cada tarefa na lista
    print(f'Tarefa: {tarefa}') # Imprime a tarefa atual
