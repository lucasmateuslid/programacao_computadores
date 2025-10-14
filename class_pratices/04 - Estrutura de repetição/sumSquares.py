import time
naturalNumber = 100
x = 1
soma = 0
calcX = 0
soma2 = 0

while x <= naturalNumber:
    xSquare = x**2
    soma2 += x
    x +=1
    soma = xSquare + soma

soma2 = soma2**2
resultado = soma2 - soma
print(f"Soma dos quadrados de 1 a {naturalNumber} é {soma}")
print(f"A soma dos números inteiros de {naturalNumber}, elevado ao quadrado é: {soma2}")
print("O valor da difereeça é: ", resultado)


