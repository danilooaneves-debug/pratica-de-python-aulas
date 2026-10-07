import random

def sorteio():
    numeros = []
    while len(numeros) < 6:
        numero = random.randint(1, 10)
        if numero not in numeros:
            numeros.append(numero)
    return sorted(numeros)

def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    return soma

sorteados = sorteio()
print("Números sorteados:", sorteados)
print("Soma dos números pares:", somapar(sorteados))