resposta=0
n=0
soma=0
while resposta != 999:
    resposta=int(input("digite um número: "))
    if resposta != 999:
        n=n+1
        soma=resposta + soma
print("A soma dos números digitados é {} e foram digitados {} números".format(soma, n))

