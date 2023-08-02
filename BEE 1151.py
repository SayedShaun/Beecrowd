def fib(n):
    a = 0
    b = 1
    lst = [a,b]
    for i in range(2,n):
        s = a+b
        a = b
        b = s
        lst.append(s)
    print(*lst)

fib(int(input()))

