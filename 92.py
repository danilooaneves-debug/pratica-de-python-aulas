infor={}
infor['nome']=str(input('nome: '))
infor['data de nascimento']=int(input('nascimento: '))
infor['carteira de trabalho']=int(input('carteira de trabalho(0 não tem:'))
except ValueError:
    print("apenas números:")
if infor['carteira de trabalho']==0:
    print('não tem carteira de trabalho')
else: 
    infor['ano de contratação']=int(input('ano de contratação:'))
    infor['salário']=float(input('salário'))
    for i,v in infor.items():
        print(F'O{i} tem valor de {v}')

