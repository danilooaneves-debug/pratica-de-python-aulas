import datetime
data_atual = datetime.date.today().year
ano = int(input("Digite o ano de nascimento: "))
idade = data_atual - ano
print("A idade é: ", idade)
if idade < 18:
    print("Ainda não é hora de se alistar") 
elif idade == 18:
    print("Está na hora de se alistar")
else:
    print("Já passou da hora de se alistar")
    print("Você deveria ter se alistado há {} anos".format(data_atual - (ano + 18)))