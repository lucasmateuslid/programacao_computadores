'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 
2-digit numbers is 9009 = 91 x 99
.

Find the largest palindrome made from the product of two 
3-digit numbers.
'''

# Encontrar o maior palindromo de 3 digitos dentro do produto de 2 digitos

# Variaveis base
valor_produto01 = 100
maiorPalindromo = 0
check = ""
eventContinuos = True
fator_a = 0
fator_b = 0


while valor_produto01 <= 999:
    valor_produto02 = 100
    while valor_produto02 <= 999:
        multiplica_produtos = valor_produto01 * valor_produto02
        print(f"O Valor dos produtos são: {valor_produto01},{valor_produto02}. Respectivamente. \n A soma dos produtos atualmente são: {multiplica_produtos}")
        check = str(multiplica_produtos)
        if check == check[::-1]:
            if multiplica_produtos > maiorPalindromo:
                maiorPalindromo = multiplica_produtos
                fator_a = valor_produto01
                fator_b = valor_produto02
                print("Maior palindromo atualizado")
        valor_produto02 += 1
    valor_produto01 += 1
print(f"O maior palindromo encontrafo foi {maiorPalindromo}. Com os produtos: {fator_a} e {fator_b}. Respectivamente.")