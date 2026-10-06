import math
numero=int(input("Digite um número: "))
conversao=int(input("qual sera a conversão? 1- binário, 2- octal, 3- hexadecimal: "))
if conversao==1:
    print("o número {} em binário é {}".format(numero,bin(numero)[2:]))
elif conversao==2:
    print("o número {} em octal é {}".format(numero,oct(numero)[2:]))       
else:
    print("o número {} em hexadecimal é {}".format(numero,hex(numero)[2:]))