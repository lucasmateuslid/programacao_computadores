mensagem = input("Digite a mensagem a ser criptografada: ")
chave = input("Digite a chave de criptografia: ")
resultado = ""

for i in range(len(mensagem)):
    char = mensagem[i]
    if char.isalpha():
        deslocamento = ord(chave[i % len(chave)].lower()) - ord('a')
        if char.islower():
            novo_char = chr((ord(char) - ord('a') + deslocamento) % 26 + ord('a'))
        else:
            novo_char = chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))
        resultado += novo_char
    else:
        resultado += char
print("Mensagem criptografada:", resultado.capitalize())

