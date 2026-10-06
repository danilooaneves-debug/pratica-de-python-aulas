import datetime
dados = []
lista = []
menor = []
maior = []

while True:
    dados.append(int(input("idade: ")))
    dados.append(input("nome: "))

    lista.append(dados[:])

    if len(lista) == 1:
        menor = lista[0]
        maior = lista[0]

    for p in lista:
        if p[0] > maior[0]:
            maior = p

        if p[0] < menor[0]:
            menor = p

    dados.clear()

    resp = input("Deseja continuar [S/N]: ").lower()

    if resp == "n":
        break

print(f"Você cadastrou {len(lista)} pessoas")

print(f"\nMaior idade: {maior[0]}")
print(f"Nome: {maior[1]}")

print(f"\nMenor idade: {menor[0]}")
print(f"Nome: {menor[1]}")
                
