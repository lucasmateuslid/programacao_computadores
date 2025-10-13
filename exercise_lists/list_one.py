   
## Q1 - Raizes de uma equação de segundo grau
print("Calculo de raizes de uma equação de segundo grau")




## Q2 - Montade de Juros acumulados após a aplicação de um capital "c", a uma taxa "i", por um tempo "t".
## Fórmula: M = C * (1 + i)^t
print("Cálculo do montante de juros acumulados após a aplicação de um capital 'c', a uma taxa 'i', por um tempo 't'.")
montante = 0
capital = float(input("Digite o valor do capital inicial: "))
taxa = float(input("Digite a taxa de juros (i): "))
tempo = float(input("Digite o tempo de aplicação (t): "))
montante = capital * (1 + taxa) ** tempo
print("O montante acumulado após", tempo, "períodos é:", montante)
print("\n")

## Q3 - Conversão de celsius para fahrenheit
print("Conversão de Celsius para Fahrenheit")

celsius = float(input("Digite a temperatura em Celsius: ")) 
fahrenheit = celsius * 9/5 + 32
print(f"A temprautra em Celsius é: {celsius}°C")
print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")
print("\n")

## Q4 - Tradução da exmpressão para calculo de programação

print("Expressão: a ← 4 + 3 . (5 + 7)")
print("Em Programação: a = 4 + 3 * (5 + 7)")
print("\n")
print("Expressão: b ← 6c – 4")
print("Em Programação: b = 6 * c - 4")
print("\n")
print("Expressão: c ← (a + 2)(x*5)")
print("Em Programação: c = (a + 2) * (x * 5)")
print("\n")
print("Expressão: e ← 2a + 5b + 4d")
print("Em Programação: e = 2 * a + 5 * b + 4 * d")
print("\n")
print("Expressão: f ← 2a + 5b + 4d")
print("Em Programação: f = 2 * a + 5 * b + 4 * d")
print("\n")

## Q5 - Indique o tipo de dado esperado na resolução de cada uma das expressões abaixo:
## (1) 4+3.(5+7) - Inteiro 
## (2) True and False - Booleano
## (3) 2>3 - Booleano
## (4) 2+3 > 5 - Booleano
## (5) "aaaa" + "3" - String


print("Tipos de dados esperados:")
print("(1) 4+3.(5+7) - Inteiro. Pois a saida aguardada é um número inteiro.")
print("(2) True and False - Booleano. Pois a saida aguardada é uma expressão lógica de verdadeiro ou falso.")
print("(3) 2>3 - Booleano. Assim como a questão anterior a saída aguardada é uma expressão lógica, assim sendo o tipo de dado booleanoo.")
print("(4) 2+3 > 5 - Booleano. Apesar do inicio da operação tratar um número inteiro, ao final faz uma comparação se o resultado do inteiro é maior que 5. \n Retornando um dado boooleano")
print('(5) "aaaa" + "3" - String. O valor retornado é um texto, então o tipo de dado retornado para ser armazenado é uma string')
print("\n")