resposta = "s"
lista=[]
while resposta == "s":
    item=it(input("digite um número: "))
    if item not in lista:
        lista.append(item)
    resposta=input('deseja continua [s/n]: ').lower()
lista.sort()
print(lista)




