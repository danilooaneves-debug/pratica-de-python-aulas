numero = "um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte"
resposta= 0 
while resposta <= 1 or resposta >= 20:
     resposta=int(input("digite um número de 1 a 20: "))
     if resposta < 1 or resposta > 20:
        print("essa resposta nn existe")
print(numero[resposta-1].upper())
       

