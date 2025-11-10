# Programa que lê um documento, define se é CPF ou CNPJ e valida o mesmo.

def validar_cpf(cpf):
    """
    Valida um CPF de 11 dígitos.
    """
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    dig1 = 0 if resto < 2 else 11 - resto
    
    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    dig2 = 0 if resto < 2 else 11 - resto
    
    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])

def validar_cnpj(cnpj):
    """
    Valida um CNPJ de 14 dígitos.
    """
    if len(cnpj) != 14 or not cnpj.isdigit():
        return False
    
    # Pesos para o primeiro dígito verificador
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    for i in range(12):
        soma += int(cnpj[i]) * pesos1[i]
    resto = soma % 11
    dig1 = 0 if resto < 2 else 11 - resto
    
    # Pesos para o segundo dígito verificador
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    for i in range(13):
        soma += int(cnpj[i]) * pesos2[i]
    resto = soma % 11
    dig2 = 0 if resto < 2 else 11 - resto
    
    return dig1 == int(cnpj[12]) and dig2 == int(cnpj[13])

try:
    # Entrada do documento CPF ou CNPJ
    documento = input("Digite o número do documento CPF ou CNPJ (somente números): ").strip()
    
    if len(documento) == 11:
        print("O documento é um CPF.")
        if validar_cpf(documento):
            print("CPF VÁLIDO!")
            print(f"\nDígitos verificadores: {documento[-2]}, {documento[-1]}, \nBase: {documento[:-2]}")

        else:
            print("CPF INVÁLIDO!")
    elif len(documento) == 14:
        print("O documento é um CNPJ.")
        if validar_cnpj(documento):
            print("CNPJ VÁLIDO!")
            print(f"\nDígitos verificadores: {documento[-2]}, {documento[-1]}, \nBase: {documento[:-2]}")
        else:
            print("CNPJ INVÁLIDO!")
    else:
        print("Número de dígitos inválido para CPF ou CNPJ.")
        
except Exception as e:
    print("Ocorreu um erro inesperado:", e)
