a=int(input( "DIGITE UM NUMERO "))
b=int(input( "DIGITE UM NUMERO "))
c=int(input( "DIGITE UM NUMERO "))
d=int(input( "DIGITE UM NUMERO "))
numeros=(a,b,c,d)
print(numeros)
print(f'o número 9 aparece {numeros.count(9)} vezes')
if a== 3 or b== 3 or c== 3 or d == 3:
    print(f'o valor 3 apareceu na posição {numeros.index(3)+1}')
else:
    print('o valor 3 não foi digitado')
pares=0
if a % 2 == 0:
    pares=pares+1
if b % 2 == 0:
    pares=pares+1
if c % 2 == 0:
    pares=pares+1
if d % 2 == 0:
    pares=pares+1
print(f'foram digitados {pares} números pares')
