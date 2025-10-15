number = int(input("Digite o valor inteiro para ser somado: "))
temp_number = number
somarValor = 0
apresentarValor = 0
contNumber = 1
while temp_number > 0:
    somarValor += temp_number % 10
    apresentarValor =  temp_number % 10
    print(f"O valor do {contNumber}° digito é: {apresentarValor}")
    contNumber +=1 
    temp_number //=10
print(f"O a soma dos digitos do inteiro digitado é: {somarValor}")
        
        