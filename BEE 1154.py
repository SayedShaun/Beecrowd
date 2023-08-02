def ages(N):
    count=0
    lst = []
    while True:
        if N<0:
            break
        else:
            count+=1
            lst.append(N)
            N = int(input())
    print(f"{(sum(lst)/count):.2f}")
            
N = int(input())
ages(N)