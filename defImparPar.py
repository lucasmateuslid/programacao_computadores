n1 = int(input("Digite o primeiro número: "))
validN1 = n1 % 2
n2 = int(input("Digite o segundo número: "))
validN2 = n2 % 2
n3 = int(input("Digite o terceiro número: "))
validN3 = n3 % 2
n4 = int(input("Digite o quarto número: "))
validN4 = n4 % 2

somarPar = 0
if validN1 == 0:
    somarPar = somarPar + n1
if validN2 == 0:
    somarPar = somarPar + n2
if validN3 == 0:
    somarPar = somarPar + n3
if validN4 == 0:
    somarPar = somarPar + n4
if somarPar > 0:
    print("A soma dos números pares é: ", somarPar)
else:
    print("Nenhum número par foi digitado.")