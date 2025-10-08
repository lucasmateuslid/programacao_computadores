number = int(input("Digite um número inteiro: "))
try:
    print(f"O número digitado foi: {1/number}")
    if number > 0:
        print("O número é positivo.")
        if number % 2 == 0:
            print(f"O número: {number} é par.")
        else:
            print(f"O número: {number} é ímpar.")  
            

except ZeroDivisionError:
    print("O número não pode ser zero.")    
    result = None    
# excepcts existem alguns tipos de excessões. 
# ZeroDivisionError
# ValueError  