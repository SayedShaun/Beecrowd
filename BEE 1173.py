def array_fill(N):
    for i in range(10):
        X = 2**i
        print(f"N[{i}] = {X*N}")
array_fill(int(input()))