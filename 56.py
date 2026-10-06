import os
media = 0
velho = 0
mulher = 0
for c in range(1, 5):
    print("="*20)
    nome = str(input("digite o nome da {}ª pessoa: ".format(c)))
    idade = int(input("digite a idade da {}ª pessoa: ".format(c)))
    sexo = str(input("digite o sexo da {}ª pessoa(M/F): ".format(c)))
    print("="*20)
    media += idade
    if velho < idade and sexo == "M":
        velho = idade
        nomevelho = nome
    if sexo=="F" and idade < 20:
        mulher += 1
    os.system('cls')

media /= 4
print("a média das idades é: {}".format(media))
print("o número de mulheres com menos de 20 anos é: {}".format(mulher))
if nomevelho:
    print("o homem mais velho é: {}".format(nomevelho))