
lista=list()
while True:
    aluno=str(input("nome:"))
    nota1=float(input('nota 1: '))
    nota2=float(input('nota 2: '))
    lista.append(aluno)
    lista.append(nota1)
    lista.append(nota2)
    print(lista)
    res=str(input('deseja continuar[S/N]: ')).lower()
    if res == 'n':
        break

