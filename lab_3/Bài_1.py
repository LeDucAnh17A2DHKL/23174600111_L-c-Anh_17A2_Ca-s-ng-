while True:
    try:
        # Nhập một số nguyên dương
        n = int(input("Nhập một số nguyên dương n: "))
        
        if n > 0:
            # Tính S1
            S1 = sum(range(1, n+1))
            
            # Tính S2
            S2 = sum(1/i for i in range(1, n+1))
            
            # Tính S3
            S3 = sum(1/(i**0.5) for i in range(2, 2*n+1, 2))
            
            # Tính S4
            S4 = sum(((-1)**i+1)/i for i in range(1, n+1))

            print(f"Số nguyên dương bạn đã nhập là {n}")
            print(f"S1 = {S1}")
            print(f"S2 = {S2}")
            print(f"S3 = {S3}")
            print(f"S4 = {S4}")

        else:
          print("Vui lòng nhập lại số nguyên dương.")
          
    except ValueError:
        print("Vui lòng nhập một số nguyên.")
