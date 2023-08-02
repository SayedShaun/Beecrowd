lst = []
for i in range(int(input())):
    X = int(input())
    lst.append(X)
    
    fib = [0,1]
    first = 0
    second = 1
    for j in range(2,X+1):
        Sum = first+second
        first = second
        second = Sum
        fib.append(Sum)
        print(F"Fib({X}) = {fib[Sum]}")



    '''if X != 0 and X != 1:
        print(f"Fib({X}) = {X-1}")
    else:
        print(f"Fib({X}) = {X}")'''