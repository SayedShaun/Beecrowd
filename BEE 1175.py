def array_change():
    lst = []
    for i in range(20):
        X = int(input())
        lst.append(X)
    index = 0
    value = -1
    for i in lst:
        print(f"N[{index}] = {lst[value]}")
        index+=1
        value-=1

array_change()