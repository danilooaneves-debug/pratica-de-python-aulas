met=[[0,0,0],[0,0,0],[0,0,0]]
ter=0
seg=0
soma=0
for c in range(0,3):
    for l in range(0,3):
        mat=int(input(f"digite um valor para [{l}, {c}]"))
        if mat % 2 ==0:
            soma+= mat
        if l==2:
            ter += mat + ter
        if c==0 and l==2:
            seg=mat
        if mat>seg:
           seg=mat
print(f"a soma dos numéros pares é {soma}")
print(f"a soma dos valores da terceira linha é {ter}")
print(f"o maior numero da segunda linha é {seg}")




  