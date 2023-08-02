def logical_sequence(X, Y):
    count = 0
    for i in range(1, Y + 1):
        count += 1
        if count == X:
            print(i)
            count = 0
        else:
            print(i, end=" ")


X, Y = map(int, input().split())
logical_sequence(X, Y)
