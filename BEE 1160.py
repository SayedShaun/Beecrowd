def function():
    T = int(input())
    for i in range(T):
        pa, pb ,g1,g2 = input().split()
        #Converting Str into int and float
        PA = int(pa)
        PB = int(pb)
        G1 = float(g1)
        G2 = float(g2)

        count_year = 0

        while PA<=PB:
            City_A = int(PA*(G1/100))
            City_B = int(PB*(G2/100))
            #increasing population every time
            PA+=City_A
            PB+=City_B
            #counting year
            count_year+=1

            if count_year>100:
                break

        if count_year>100:
            print("Mais de 1 seculo.")

        else:
            print(f"{count_year} anos.")

function()
