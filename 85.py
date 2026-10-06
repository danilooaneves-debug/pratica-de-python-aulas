lista=[[],[]]
valor=0

for p in range(0,7):
    valor=(int(input(f"digite o {p+1}n: ")))
    if valor % 2 ==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
sorted(lista[0])
sorted(lista[1])
print(lista)