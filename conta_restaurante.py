valorConta = float(input("Digite o valor da conta do cliente: "))
valorRecebido = float(input("Digite o valor recebido pelo cliente: "))
# Calcula o troco
troco = valorRecebido - valorConta
# Considerando só a parte inteira do troco
troco_int = int(troco)

n200 = troco_int // 200
troco_int = troco_int % 200

n100 = troco_int // 100
troco_int = troco_int % 100

n50 = troco_int // 50
troco_int = troco_int % 50

n20 = troco_int // 20
troco_int = troco_int % 20

n10 = troco_int // 10
troco_int = troco_int % 10

n5 = troco_int // 5
troco_int = troco_int % 5

n2 = troco_int // 2
troco_int = troco_int % 2

n1 = troco_int // 1

if troco >= 1:
    print("Troco total: R$", troco)
    print("Cédulas para devolver: ")
    if n200 >= 1:
        print("Notas de 200: ", n200)
    if n100 >= 1:
        print("Notas de 100: ", n100)
    if n50 >= 1:
        print("Notas de 50: ", n50)
    if n20 >= 1:
        print("Notas de 20: ", n20)
    if n10 >= 1:
        print("Notas de 10: ", n10)
    if n5 >= 1:
        print("Notas de 5: ", n5)
    if n2 >= 1:
        print("Notas de 2: ", n2 )
    if n1 >= 1:
        print("Moedas de 1: ", n1)
elif troco < 0 :
    print("A cozinha ta cheia de louça pra lavar")
else:
    print("Sem valores a devolver.")