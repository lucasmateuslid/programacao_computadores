numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(12)]

somarPar = sum(n for n in numeros if n % 2 == 0)
somarImpar = sum(n for n in numeros if n % 2 != 0)

if somarPar > 0:
    print("A soma dos números pares é:", somarPar)
if somarImpar > 0:
    print("A soma dos números ímpares é:", somarImpar)
if somarPar == 0 and somarImpar == 0:
    print("Nenhum número foi digitado.")
