import time

def contador():
    cont = 0
    while True:
        cont += 1
        if cont > 10:
            break
        yield cont

def reverso():
    cont = 11
    while True:
        cont -= 1
        if cont < 1:
            break
        yield cont

def main(inicio, fim, passo):
    if passo == 0:
        raise ValueError("O passo não pode ser zero")

    cont = inicio
    while (passo > 0 and cont <= fim) or (passo < 0 and cont >= fim):
        yield cont
        cont += passo

def mostrar(titulo, valores, pausa=0.5):
    print(titulo, end=' ', flush=True)
    for v in valores:
        print(v, end=' ', flush=True)
        time.sleep(pausa)
    print()  # pula a linha no final

mostrar("Contador:", contador())
mostrar("Contador reverso:", reverso())

input1 = int(input("Digite o valor inicial: "))
input2 = int(input("Digite o valor final: "))
input3 = int(input("Digite o valor do passo: "))
mostrar("Contagem:", main(input1, input2, input3))