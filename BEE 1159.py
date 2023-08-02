def function():
    while True:
        X = int(input())
        if X == 0:
            break
        else:
            count = 0
            lst = []
            while count<5:
                if X%2==0:
                    lst.append(X)
                    count+=1
                X+=1
            print(sum(lst))
function()