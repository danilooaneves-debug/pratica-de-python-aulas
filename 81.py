
numeros = []

for cont in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for i in range(4):
    for j in range(i + 1, 5):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print(numeros)


