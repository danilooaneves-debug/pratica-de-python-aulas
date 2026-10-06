import datetime


ano=int(input("Digite o ano de nascimento: "))
data_atual = datetime.date.today().year
idade = data_atual - ano
if idade <= 9:
    print("MIRIM")
elif idade <= 14:      
    print("INFANTIL")
elif idade <= 19:   
    print("JUNIOR")
else:   
    print("MASTER")
    