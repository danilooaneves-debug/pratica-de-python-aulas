boletim = {}

boletim['nome']=str(input('nome:'))
boletim['média']=float(input('média:'))
if boletim['média']<=6:
    print('reprovado'
          )
else:
    print('aprovado')