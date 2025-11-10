# Programa que le um documento, define se é CPF ou CNPJ e valida o mesmo.
soma = 0
multiplicador = 2
resto = 0
try:
    # Entrada do documento CPF ou CNPJ
    documento_number = input("Digite o número do documento CPF ou CNPJ (somente números): ")

    # Validador do tipo de Documento
    if len(documento_number) == 11:
        print("O documento é um CPF.")
        tipo_documento = "CPF"
    elif len(documento_number) == 14:
        print("O documento é um CNPJ.")
        tipo_documento = "CNPJ"
    else:
        print("Número de dígitos inválido para CPF ou CNPJ.")
        tipo_documento = "Inválido"
    
    
    # Conversão da entrada para inteiro
    documento_number = int(documento_number)
    digito_verificador_2 = documento_number % 10
    digito_verificador_1 = (documento_number // 10) % 10
    documento_base = documento_number
    documento_number //= 100
    # Confirmação de entrada para o usuário.
    print(f"\nDígitos verificadores: {digito_verificador_1}, {digito_verificador_2}, \nBase: {documento_number}")
    
    if tipo_documento == "CPF":
        # Extraindo valores temporários para cálculo
        tempo_num1 = documento_number
        tempo_num2 = documento_base // 10
        # Cálculo do 1º dígito verificador do CPF
        
        while tempo_num1 > 0:
            soma += (tempo_num1 % 10) * multiplicador # Pego o último digito
            tempo_num1 //= 10 # Removo o último digito
            multiplicador += 1
            # Fim do loop
        
        resto = soma % 11
        if resto < 2:
            digito_calculado_1 = 0
        elif resto >= 2:
            digito_calculado_1 = 11 - resto
        print("\n1º Dígito calculado: ", digito_calculado_1)
        
        # Resetando variáveis para o próximo cálculo
        soma = 0
        multiplicador = 2
        
        # Cálculo do 2º dígito verificador do CPF
        while tempo_num2 > 0 and multiplicador <= 11:
            soma += (tempo_num2 % 10) * multiplicador # Pego o último digito
            tempo_num2 //= 10 # Removo o último digito
            multiplicador += 1 
        resto = soma % 11
        if resto < 2:
            digito_calculado_2 = 0
        elif resto >= 2:
            digito_calculado_2 = 11 - resto
        print("\n2º Dígito calculado: ", digito_calculado_2)
        
        if digito_calculado_1 == digito_verificador_1 and digito_calculado_2 == digito_verificador_2:
            print("CPF VÁLIDO!")
        else:
            print("CPF INVÁLIDO!")
            
    elif tipo_documento == "CNPJ":
        # Calculo do 1º dígito verificador do CNPJ
        print(documento_number)
        print(documento_base)
        # Extraindo valores temporários para cálculo
        tempo_num1 = documento_number
        tempo_num2 = documento_base // 10
        multiplicador = 2   
        
        while tempo_num1 > 0:
            soma += (tempo_num1 % 10) * multiplicador # Pego o último digito
            tempo_num1 //= 10 # Removo o último digito
            multiplicador += 1
            if multiplicador > 9:
                multiplicador = 2
            # Fim do loop
        resto = soma % 11
        if resto < 2:
            digito_calculado_1 = 0
        elif resto >= 2:
            digito_calculado_1 = 11 - resto 
        print("\n1º Dígito calculado: ", digito_calculado_1)
        # Resetando variáveis para o próximo cálculo
        soma = 0
        multiplicador = 2   
        # Cálculo do 2º dígito verificador do CNPJ
        while tempo_num2 > 0:
            soma += (tempo_num2 % 10) * multiplicador # Pego o último digito
            tempo_num2 //= 10 # Removo o último digito
            multiplicador += 1
            if multiplicador > 9:
                multiplicador = 2
            # Fim do loop
        resto = soma % 11
        if resto < 2:
            digito_calculado_2 = 0
        elif resto >= 2:
            digito_calculado_2 = 11 - resto
        print("\n2º Dígito calculado: ", digito_calculado_2)
        
        if digito_calculado_1 == digito_verificador_1 and digito_calculado_2 == digito_verificador_2:
            print("CNPJ VÁLIDO!")
        else:
            print("CNPJ INVÁLIDO!")
    else:
        print("Não foi possível validar o documento devido ao número de dígitos inválido.")    
        
        

    

    
except ValueError:
    print("O valor digitado não é um número inteiro.")
except Exception as e:
    print("Ocorreu um erro inesperado:", e)
    