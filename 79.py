numeros=[]
maior=0
menor=10000000000000
for cont in range(5):
    numero=(int(input("digite um número: ")))
    numeros.append(numero)
    if numero > maior: 
        maior=numero 
    if numero < menor:
        menor=numero 

print(f"o maior núemro foi {maior} na posição {numeros.index(maior)+1}")
print(f"o maior núemro foi {menor} na posição {numeros.index(menor)+1}")
print(numeros)
         




