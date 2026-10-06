n= soma = media = menor = maior = 0
resposta=str
while resposta != "N":
   numero=int(input("Digite um número: "))
   n += 1
   soma=numero + soma
   media=soma/n
   if n == 1:
       menor = maior = numero
   else:
        if menor >= numero:
           menor=numero
        if maior <= numero:
           maior=numero
   resposta=(str(input("Deseja continuar? [S/N] "))).upper()
print("A média dos números digitados é {}, o maior número digitado foi {} e o menor número digitado foi {}".format(media, maior, menor))