i = 2
while i < 100:
    j = 2
    prime = True
    while j * j <= i:
        if i % j == 0:
            prime = False
            break
        j += 1
    
    if prime:
        print(i)
    
    i += 1
