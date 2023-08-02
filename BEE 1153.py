def factorial(N):
    if N==0:
        return 1
    else:
        return N*factorial(N-1)
    
result = factorial(int(input()))
print(result)