n = int(input("Digite o valor para verificar se é um Palindromo: "))
soma = 0
new_n = n
while n >0:
    ultimodig = n%10
    soma = (soma*10)+ultimodig
    n = n //10
if soma == new_n:
    print("Palindromo")
else:
    print("Não é Palindromo")