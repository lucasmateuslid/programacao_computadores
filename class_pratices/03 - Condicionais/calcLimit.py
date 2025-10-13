try: 
    limitNumber = int(input("Digite o número inteiro, limite inteiro para somar: "))
    numberCalc = 0 
    sucessorXcalc = 0
    while sucessorXcalc < limitNumber:
        sucessorXcalc = sucessorXcalc + 1
        numberCalc = numberCalc + sucessorXcalc
    print("A soma dos números é: ", numberCalc)

except ValueError:
    print("O valor digitado não é um número inteiro.") 