cont = 0 # contador recebe 0, 
minValue = 1000 # Valor minimo, aonde inicia a contagem.
while minValue <= 10000: # Enquanto o valor minimo for menor ou igual a 10.000, o loop continuará.
    if (minValue%3) == 0: # Condicional que verifica 
        cont+=1
    minValue+=1
print(cont)