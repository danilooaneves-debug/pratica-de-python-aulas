#sorteando 4 dados
from random import randint
geral=list()
for c in range (0,4):
    dados={}
    dados[c]=randint(0,6)
    geral.append(dados.copy())
print(dados)
print(geral)
for j,r in geral:
    print(f'jogador núemero{geral[j]} tirou{geral[r]} no dado')
