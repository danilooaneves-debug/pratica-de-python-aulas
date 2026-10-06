maior=0
menor=1000
for c in range (1,6):
    peso=float(input("digite o peso da {}ª pessoa: ".format(c)))
    if peso > maior:
        maior=peso
    if peso < menor:
        menor=peso  
print("o maior peso é {}kg".format(maior))
print("o menor peso é {}kg".format(menor))


    