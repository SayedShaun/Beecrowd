def function(N):
    for i in range(N):
        X,Y = map(int,input().split())
        lst = []
        count = 0
        while count<Y:
            if X%2 !=0:
                lst.append(X)
                count+=1
            X+=1
        print(sum(lst))

function(int(input()))