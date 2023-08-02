def func(A,N):
    if N<=0:
        get = N= int(input())
        return get
    else:
        Sum = 0
        for i in range(N):
            Sum+=A+i
        print(Sum)

A,N = map(int,input().split())
func(A,N)