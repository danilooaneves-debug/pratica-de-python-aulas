from random import randint
a=(randint(0,9), randint(0,9),randint(0,9))
b=(randint(0,9),randint(0,9))
c=a+b
menor=10
maior=0

for numero in c:
    if numero > maior:
        maior=numero
    if numero < menor:
        menor=numero
print 
print(c)
print(f"o menor núemro foi {menor}")
print(f"o maior número foi {maior}")



    


