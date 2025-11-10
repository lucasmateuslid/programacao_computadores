n = 0
for n in range (1,10):
    print(f"Starting n value: {n}")
    while n > 1:
        print(f"Current n value: {n}")
        if n%2 == 0:
            n=n//2
        else:
            n=3*n+1

