import datetime
ano=datetime.datetime.now().year
maior = 0
menor = 0
for c in range(0,7):
    nascimento=int(input("digite o ano de nascimento: "))
    if nascimento-ano>=18:
        maior+=1
    else: 
        menor+=1
print("maiores de idade: {}".format(maior))
print("menores de idade: {}".format(menor))