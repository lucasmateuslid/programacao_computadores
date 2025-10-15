# Prgramar ira sortear o número da sorte, e perguntará ao usuário para tentar adivinhar até acertar o número.
# Progarama de repetiçãp que recebe 2 valores 1 superior outro inferior, e sorteia um número entre esses valores.
# O usuário deve tentar adivinhar o número sorteado, e o programa irá informar se o número é maior ou menor, até que o usuário acerte o número.
# A lógica do programa é baseada em um loop aonde toda vez que o usuário informa um número que se estiver abaixo do número, atualiza o novo número inferior
# E se o número informado for maior, atualiza o número superior.
# No momemnto em que o usuário acerta o número, o loop é interrompido e o programa informa que o usuário acertou o número.


import random
numeroSorteado = random.randint(1, 100) # Sorteia um número entre 1 e 100
gameStarted = True;
limiteInferior = 1
limiteSuperior = 100

while gameStarted: 
    try:
        numeroUsuário = int(input(f"Digite um número entre {limiteInferior} e {limiteSuperior}: "))
        if numeroUsuário < limiteInferior or numeroUsuário > limiteSuperior: # Verifica se o número está dentro do intervalo.
            print(f"Número inválido, digite um número entre {limiteInferior} e {limiteSuperior}.")
        elif numeroUsuário < numeroSorteado: 
            print("O número é maior que", numeroUsuário)
            limiteInferior = numeroUsuário 
        elif numeroUsuário > numeroSorteado:
            print("O número é menor que", numeroUsuário)
            limiteSuperior = numeroUsuário # Atualiza o limite superior para o número informado - 1
        else: 
            print("Parabéns! Você acertou o número:", numeroSorteado)
            print(f"O Valor secreto era {numeroSorteado}")
            gameStarted = False; # Encerra o jogo.
    except ValueError:
        print("Valor inválido, digite um número inteiro entre 1 e 100.")
