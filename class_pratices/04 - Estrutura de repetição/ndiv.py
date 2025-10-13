"""
Para conseguir fazer uma repetição, é ncessário identificar padrões de repetições.
Uma boa prática é analisar o prolema e identificar aonde se repete, como se repete e se é possível adicionar um padrão.
Caso seja identificado um padrão, é possível utilizar uma estrutura de repetição.
"""

#Abaixo um exemplo de estrutura de repetição para identificar o número divisores e checar se o valor inserido é primo.
checkNumber = int(input("Digite um número para verificar divisor: "))
ndiv = 0 
x = 1
while x < checkNumber: # Se o valor for menor igual ao valor inserido, o loop vai parar e não adicionar mais 1 valor.
    if checkNumber % x == 0: 
        ndiv += 1 # Adiciona 1 ao valor de ndiv, a string do número de divisiores. Como está subordinado ao IF e ao While, irá repetir até chegar ao valor inserido.
    x += 1 # Adiciona 1 ao valor de x, para que o loop avance e seja possível adicionar mais 1 valor para verificar se é divisor.
print("O número de divisores é: ", ndiv)
if ndiv == 2: # Se o número de divisores limitar e for igual a 2, o esse "Se" irá imprimir a informação que o valor "checkNumber" é primo.
    print(f"O número: {checkNumber} é primo.")
else:
    print("O número inserido não é primo.")
    