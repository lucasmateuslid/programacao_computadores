import time 
x = 1
while True:
    ndiv = 0 
    y = 1
    while y < x: # Se o valor for menor igual ao valor inserido, o loop vai parar e não adicionar mais 1 valor.
        if x % y == 0: 
            ndiv += 1 # Adiciona 1 ao valor de ndiv, a string do número de divisiores. Como está subordinado ao IF e ao While, irá repetir até chegar ao valor inserido.
        y += 1 # Adiciona 1 ao valor de x, para que o loop avance e seja possível adicionar mais 1 valor para verificar se é divisor.
    print("O número de divisores é: ", ndiv)
    if ndiv == 2: # Se o número de divisores limitar e for igual a 2, o esse "Se" irá imprimir a informação que o valor "x" é primo.
        print(f"O número: {x} é primo.")
        time.sleep(1)
    else:
        print(f"O número inserido {x} não é primo.")
        time.sleep(1)
x += 1