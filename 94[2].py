dados = list()
cadastro = dict()
pessoas=0
idade=0
mulher=list()
while True:
    cadastro['nome'] = str(input("digite o nome: "))
    cadastro['idade'] = int(input('digite a idade: '))
    idade+= cadastro['idade'] 
    while True:
        cadastro['sexo'] = input("digite o sexo [M/F]: ").lower()
        if cadastro['sexo'] in ['m', 'f']:
            break
        else:
            print("digite apenas M ou F")
    if cadastro['sexo'] == 'f':
        mulher.append(cadastro['nome'])
            

    dados.append(cadastro.copy())

    while True:
        resp = input("deseja continuar [S/N]: ").strip().lower()
        if resp in ['s', 'n']:
            break
        else:
            print("digite apenas S ou N")
    pessoas+=1
    if resp == 'n':
        break
média=(idade/pessoas)
print(f"o total de pessoas cadastradas foram{pessoas}")
print(f"a média de idade foi de {média}")
print(f'as mulheres registradas foram {mulher}')
for c in dados:
    if c['idade'] > média:
        print(f"{c['nome']} está acima da média, com {c['idade']} anos")
