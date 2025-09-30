valorConta = float(input("Digite o valor da conta do cliente: "))
valorRecebido = float(input("Digite o valor recebido pelo cliente: "))

troco = valorRecebido - valorConta
print("\nTroco total: R$ {:.2f}".format(troco))

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

print("\nCédulas para devolver:")
print("Notas de 200:", n200)
print("Notas de 100:", n100)
print("Notas de 50:", n50)
print("Notas de 20:", n20)
print("Notas de 10:", n10)
print("Notas de 5:", n5)
print("Notas de 2:", n2)
print("Notas de 1:", n1)