# Prgramar ira sortear o número da sorte, e perguntará ao usuário para tentar adivinhar até acertar o número.
# Progarama de repetiçãp que recebe 2 valores 1 superior outro inferior, e sorteia um número entre esses valores.
# O usuário deve tentar adivinhar o número sorteado, e o programa irá informar se o número é maior ou menor, até que o usuário acerte o número.
# A lógica do programa é baseada em um loop aonde toda vez que o usuário informa um número que se estiver abaixo do número, atualiza o novo número inferior
# E se o número informado for maior, atualiza o número superior.
# No momemnto em que o usuário acerta o número, o loop é interrompido e o programa informa que o usuário acertou o número.
import random
gameStarted = True
limiteInferior = 1
contador_tentativas = 0 
seletor_dificuldade = int(input("Selecione a dificuldade (Fácil (1), Médio (2), Difícil (3), Impossível (4)): "))

if seletor_dificuldade == 1:
    max_tentativas = 99
    print_tentativas = max_tentativas
    limiteSuperior = 100
elif seletor_dificuldade == 2:
    max_tentativas = 50
    print_tentativas = max_tentativas
    limiteSuperior = 1000
elif seletor_dificuldade == 3:
    max_tentativas = 25
    print_tentativas = max_tentativas    
    limiteSuperior = 10000
elif seletor_dificuldade == 4:
    max_tentativas = 15
    print_tentativas = max_tentativas
    limiteInferior = -500000
    limiteSuperior = 500000

numero_usuario = random.randint(limiteInferior, limiteSuperior) # Sorteia um número entre 1 e 100


while gameStarted: 
    try:
        if contador_tentativas > max_tentativas:
            print(f"Tentativas excedidas. ")
            gameStarted = False
        numeroUsuário = int(input(f"Digite um número entre {limiteInferior} e {limiteSuperior}: "))
        if numeroUsuário < limiteInferior or numeroUsuário > limiteSuperior: # Verifica se o número está dentro do intervalo.
            print(f"Número inválido, digite um número entre {limiteInferior} e {limiteSuperior}.")
            contador_tentativas += 1
        elif numeroUsuário < numero_usuario: 
            print("O número é maior que", numeroUsuário)
            limiteInferior = numeroUsuário 
            contador_tentativas += 1
        elif numeroUsuário > numero_usuario:
            print("O número é menor que", numeroUsuário)
            limiteSuperior = numeroUsuário # Atualiza o limite superior para o número informado - 1
            contador_tentativas += 1
        else: 
            print("Parabéns! Você acertou o número")
            print(f"O Valor secreto era {numero_usuario}")
            print(f"Você acertou em {contador_tentativas} tentativas.")
            gameStarted = False; # Encerra o jogo.
    except ValueError:
        print("Valor inválido, digite um número inteiro entre 1 e 100.")
