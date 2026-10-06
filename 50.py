pares = 0
impares = 0
for c in range(0,6):
    n=int(input("Digite um número: "))
    if n%2==0:
        pares += n
    else:
        impares += n
print("soma de números pares: {}".format(pares))
print("soma de números ímpares: {}".format(impares))
