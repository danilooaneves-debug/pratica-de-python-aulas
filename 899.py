#pergunta os nomes
lista=list()
while True:
    aluno=str(input("nome:"))
    nota1=float(input('nota 1: '))
    nota2=float(input('nota 2: '))
    lista.append([aluno, nota1, nota2])
    res=str(input('deseja continuar[S/N]: ')).lower()
    if res == 'n':
        break
#calcular a media
for i, aluno in enumerate(lista, start=1):
    media=(aluno[1]+aluno[2])/2
    print(f'{i}a nota do {aluno[0]} foi {media}')

z=input('deseja ver a nota de qual aluno?')
print(lista[z][0])