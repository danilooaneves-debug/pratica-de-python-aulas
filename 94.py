dados=list()
cadastro=dict()
while True:
    cadastro['nome']=str(input("digite o nome"))
    cadastro['sexo']=input("digite o sexo[M/F]").lower
    if cadastro['sexo'] != "M".lower or "F".lower:
        print("digite apenas M ou F")
        cadastro['sexo']=input("digite o sexo[M/F]").lower    
    resp=input("deseja continura [S/N]").lower
    if resp!='s' or 'n':
        print("digite apenas S ou N")
    if resp=='n':
        break
     

   

   