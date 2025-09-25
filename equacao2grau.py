a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))


# Calcular o valor de delta
delta_final = b**2 - 4*a*c
raizDelta = delta_final**0.5
calc_doisa = 2*a
# Calculo de x1 


x1 = (-b+raizDelta)/calc_doisa
x2 = (-b-raizDelta)/calc_doisa
print("As raizes da equação são: x1 =", x1," x2 = ",x2)


print("A raiz de Delta: ", raizDelta)
print("Valor de delta: ", delta_final)