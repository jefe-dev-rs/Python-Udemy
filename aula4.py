total_procoes = int(input('Quantas porções o produto tem? '))
porcoes_por_dia = int(input('Quantas porções você consome por dia? '))
dias = total_procoes / porcoes_por_dia

print(f'O produto vai durar {int(dias)} dias') # convertendo para inteiro
print(f'O produto vai durar {dias:.0f} dias') # arredondando para 0 casas decimais