
gremio = inter = draw = grenais = 0

while True:
    Inter, Gremio = map(int,input().split())
    print("New grenal (1-yes 2-no)")

    if Inter>Gremio:
        inter+=1
    elif Inter == Gremio:
        draw+=1
    else:
        gremio+=1

    grenais+=1

    N = int(input())
    if N == 1:
        continue
    else:
        break

print(f"""{grenais} grenais
Inter:{inter}
Gremio:{gremio}
Empates:{draw}""")

if inter==gremio:
    print("Nao houve vencedor")
else:
    if inter>gremio:
        print("Inter venceu mais")
    else:
        print("Gremio venceu mais")
