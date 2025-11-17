from random import choice

simbolos = "XaTUKliJk10912&%*!+"
senha = ""

for pos in range(16):
    senha = senha + choice(simbolos)
print(senha)
    
acertou = False
tentativas = 0

while (acertou == False) and (tentativas < 3):
    senha_usuario = input("Digite a senha: ")
    if senha == senha_usuario:
        acertou = True 
    tentativas += 1
if acertou == True:
    print("Acertou em: ", tentativas," tentativas")
else:
    print("Número de tentativas excedido!!!")    

    