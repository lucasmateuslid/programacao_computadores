nValue = 0 
tam = 0
maiorSequencia = 0
try:
    for k in range(1,150):
        nValue = k    
        print(f"\nStarting n value: {nValue}")
        # Collatz Conjecture Loop
        while nValue != 1:
            print(nValue, end=" --> ")
            if nValue % 2 == 0:
                nValue = nValue // 2
            else:
                nValue = 3 * nValue + 1
            tam += 1            
        # Fim do loop
        if tam > maiorSequencia:
            maiorSequencia = tam
    print(f"\nTotal steps in the longest sequence: {maiorSequencia} for starting n value: {k}")
    print("\nCollatz Conjecture sequence completed.")
except ValueError:
    print("Invalid input! Please enter an integer number.")
except Exception as e:
    print("An unexpected error occurred:", str(e))  