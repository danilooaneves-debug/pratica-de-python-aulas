c=1
numero=int(input("digite um número: "))
limite=int(input("digite quantos termos da sequencia voce quer: "))
while c <= limite:
    print(numero, end=" ")
    numero=numero+1
    c += 1
print("Fim")