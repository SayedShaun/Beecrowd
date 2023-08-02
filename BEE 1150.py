def Exceeding_Z(X,Z):
    while Z<=X:
            Z = int(input())
    Sum = X
    count = 1
    while Sum <= Z:
        X += 1
        Sum += X
        count += 1
    print(count)      

X = int(input())
Z = int(input())
Exceeding_Z(X,Z)