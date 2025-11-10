name = input("Digite seu nome: ")
nameInverted = ""
for i in range(len(name) - 1, -1, -1): # Inverte o nome usando um loop for e range para iterar de trás para frente
    nameInverted += name[i]
print("Nome invertido:", nameInverted)

name = name.replace(" ", "").lower()
nameInverted = nameInverted.replace(" ", "").lower()

if name == nameInverted:
    print("Seu nome é um palíndromo!")
else:
    print("Seu nome não é um palíndromo.")