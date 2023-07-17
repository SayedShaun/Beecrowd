def growing_sequence(X):
    while True:
        if X == 0:
            break
        else:
            lst = []
            for i in range(1, X + 1):
                lst.append(i)
            print(' '.join(map(str, lst)))
        X = int(input())


X = int(input())
growing_sequence(X)
