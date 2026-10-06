fatorial=1
resposta=0
numero=int(input("digite um número: "))
c=1
while resposta != "S":
 while c<=numero:
    fatorial=fatorial*c
    c=c+1
 print("o fatorial de {} é {}".format(numero, fatorial))
resposta=str(input("deseja continuar? [S/N] ")).upper()
    