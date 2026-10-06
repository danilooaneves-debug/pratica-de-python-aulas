genero=0
while genero != "M" and genero != "F":
    genero=str(input("qual o seu genero? [M/F] ")).strip().upper()
    if genero != "M" and genero != "F":
        print("digite apenas M ou F")
print("seu genero é {}".format(genero))
