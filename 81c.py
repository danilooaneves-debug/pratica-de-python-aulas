lista=[]
resposta="s"
while resposta=="s":
    numero=int(input("digite um número: "))
    lista.append(numero)
    resposta=str(input("deseja continuar [S/N]").lower())
print(f"a lista contém {len(lista)} elementos")
print(sorted(lista, reverse=True))
if 5 in lista:
    print("o número 5 esta na lista")