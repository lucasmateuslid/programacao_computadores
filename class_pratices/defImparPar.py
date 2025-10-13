n1 = int(input("Digite o primeiro número: "))
validN1 = n1 % 2
n2 = int(input("Digite o segundo número: "))
validN2 = n2 % 2
n3 = int(input("Digite o terceiro número: "))
validN3 = n3 % 2
n4 = int(input("Digite o quarto número: "))
validN4 = n4 % 2

somarPar = 0
somarImpar = 0 

if somarPar == 0:
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
if somarImpar == 0:
    if validN1 != 0:
        somarImpar = somarImpar + n1
    if validN2 != 0:
        somarImpar = somarImpar + n2
    if validN3 != 0:
        somarImpar = somarImpar + n3
    if validN4 != 0:
        somarImpar = somarImpar + n4
    print("A soma dos números ímpares é: ", somarImpar)
else:
    print("Nenhum número foi digitado.")
