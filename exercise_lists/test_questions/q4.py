# Programa que recebe sucessivamente números inteiros maiores ou iguais a zero. Quando digitado um número negativo, o programa para de pedir números e exibe a quantiade de números impares digitados, a média dos valores pares digitados e a média de todos os valores digitados

programa_roda = True

somarPar = 0
countPar = 0
countImpar = 0
countGeral = 0
somarGeral = 0

while programa_roda:
        numero_usuario = int(input("Digite um numero inteio: "))
        if numero_usuario < 0:
            programa_roda = False
        else:        
            if (numero_usuario%2) == 0:
                somarPar += numero_usuario
                countPar += 1
            else:
                countImpar += 1
            countGeral += 1
            somarGeral += numero_usuario
        
mediaGeral = somarGeral/countGeral
mediarPar = somarPar/countPar

print(f"A quantiade de Números impares digitados: {countImpar}. \n Média dos Valores pares digitados: {mediarPar}. \n Média geral dos valores: {mediaGeral}.")        
