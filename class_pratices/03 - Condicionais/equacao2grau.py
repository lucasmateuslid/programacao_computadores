a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))


if a == 0:
    print("Não é uma equação de segundo grau")
else:
    # Calcular o valor de delta
    delta_final = b**2 - 4*a*c
    if delta_final < 0:
        print("Não existem raizes reais")
    else:
        raizDelta = delta_final**0.5
        calc_doisa = 2*a
        x1 = (-b+raizDelta)/calc_doisa
        x2 = (-b-raizDelta)/calc_doisa
        if delta_final > 0:
            print("As raizes da equação são: x1 =", x1," x2 = ",x2)
        else:
            print("Só existe 1 raiz válida: ", x1)

