entradaSeg1 = float(input("Digite o valor inicial do primeiro segmento: "))
entradaSeg2 = float(input("Digite o valor final do primeiro segmento: "))
entradaSeg3 = float(input("Digite o valor inicial do segundo segmento: "))
entradaSeg4 = float(input("Digite o valor final do segundo segmento: "))


#Conferencia se possue sobreposição
if entradaSeg2 >= entradaSeg3 and entradaSeg4 >= entradaSeg1:
    print("Os segmentos se sobrepõem.")
    print("Primeiro segmento: [", entradaSeg1, ",", entradaSeg2, "]")
    print("Segundo segmento: [", entradaSeg3, ",", entradaSeg4, "]")
    print("Os segmentos se sobrepõem no intervalo: [", max(entradaSeg1, entradaSeg3), ",", min(entradaSeg2, entradaSeg4), "]")
    print("O comprimento da sobreposição é: ", min(entradaSeg2, entradaSeg4) - max(entradaSeg1, entradaSeg3))
#Se não possue sobreposição
elif entradaSeg2 < entradaSeg3 or entradaSeg4 < entradaSeg1:
    print("Os segmentos não se sobrepõem.")
    print("Primeiro segmento: [", entradaSeg1, ",", entradaSeg2, "]")
    print("Segundo segmento: [", entradaSeg3, ",", entradaSeg4, "]")
    print("Não há intervalo de sobreposição.")