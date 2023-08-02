Alcool = Gasolina = Diesel = 0
while True:
    x = int(input())

    if x < 1 or x > 4:
        continue
    else:
        if x == 1:
            Alcool += 1
        elif x == 2:
            Gasolina += 1
        elif x == 3:
            Diesel += 1
        else:
            break
print("MUITO OBRIGADO")
print(f"""Alcool: {Alcool}
Gasolina: {Gasolina}
Diesel: {Diesel}""")
