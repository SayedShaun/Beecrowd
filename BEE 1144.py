def function(N):
    for i in range(1, N + 1):
        print(f"{i} {(i ** 2)} {(i ** 3)}")
        print(f"{i} {(i ** 2) + 1} {(i ** 3) + 1}")


function(int(input()))
