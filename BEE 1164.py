def function():
    for i in range(int(input())):
        X = int(input())
        
        if X>0 and X%2==0:
            #lst.append(X)
            lst = []
            for i in range(1,X):
                if X%i==0:
                    lst.append(i)

            sum_total = sum(lst)
            if X == sum_total:
                print(f"{X} eh perfeito")
            else:
                print(f"{X} nao eh perfeito")
        else:
            print(f"{X} nao eh perfeito")

function()
