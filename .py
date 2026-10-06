lista=[]
par=[]
impar=[]
resposta="s"
while resposta=="s":
    numero=int(input("digite um número: "))
    lista.append(numero)
    if numero%2==0:
        par.append(numero)
    if numero%2==1:
        impar.append(numero)
    resposta=str(input("deseja continuar [S/N]").lower())
print(lista)
print(par)
print(impar)

