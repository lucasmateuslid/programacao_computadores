#Programa em Python que exiba o quinto número divisivel por 13 e por 7
numeroDivisivel = 0
quintNumero = 0
resultado = 0
programa_roda = True
while programa_roda:
    if quintNumero == 5:
        resultado = numeroDivisivel
        programa_roda = False
    else:
        if (numeroDivisivel%13) == 0 and (numeroDivisivel%7) == 0:
            quintNumero += 1 
            resultado = numeroDivisivel
            numeroDivisivel += 1
        else:
            numeroDivisivel += 1
print("O quinto numero divisivel por 13 e 7 ao mesmo tempo é: ", resultado)
