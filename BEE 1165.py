def prime_number():
    for i in range(int(input())):
        X = int(input())
        if X>1:
            for i in range(2,X):
                if X%i==0:
                    print(f"{X} nao eh primo")
                    break
                else:
                    print(f"{X} eh primo")
        else:
            print(f"{X} nao eh primo")
prime_number()