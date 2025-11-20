# Aula de repetição - Laços de Repetição

# Laço for / Quando a quantidade de repetições é conhecida
for i in range(5): # range(5) gera uma sequência de números de 0 a 4
    print("Iteração em For deu número:", i)

# Laço while / Quando a quantidade de repetições é desconhecida
i = 0
while i < 5: # enquanto i for menor que 5
    print("Iteração em While deu número:", i)
    i += 1 # incrementa i em 1 a cada iteração

# Exemplo prático com while
senha = ' ' # inicializa a variável senha com um valor vazio
while senha != 'python123': # enquanto a senha for diferente de 'python123'
    senha = input("Digite a senha correta: ") # pede para o usuário digitar a senha
print("Senha correta! Acesso permitido.")  # quando a senha correta for digitada




