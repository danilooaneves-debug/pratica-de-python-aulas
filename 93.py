jogador = {}
gols = list()
todos= list()
total=0
while True:
    jogador.clear()
    c=0
    jogador["nome"] = input("digite o nome do jogador: ")
    partidas = int(input(f"quantas partidas {jogador['nome']} jogou: "))
    while c < partidas:
        n = int(input(f"quantos gols na partida {c + 1}: "))
        gols.append(n)
        c += 1
        total += n
        jogador["gols"] = gols
        jogador['total']=total
    todos.append(jogador.copy())
    resp=str(input("deseja continuar [S/N]")).lower()
    if resp == 'n':
        break
print(30*'=')
print("cod nome" "gols" "total")
for p in todos:
    for k,v in jogador.items():
        print(f"{p}{p[k]}{p[v]}")













#print(jogador)
#print(30*'=')
#for k,v in jogador.items():
#        print(f"no campo {k} tem o valor {v}" )
#for p,o in enumerate(gols):
#print(f"no jogo {p} fez {o} gols")