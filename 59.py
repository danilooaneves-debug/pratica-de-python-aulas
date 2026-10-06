print("calculadora")
resposta=0
while resposta !=5:
   n1=int(input("digite um número: "))
   n2=int(input("digite outro número: "))
   print("escolha uma das opções abaixo: ")
   print("="*20)
   print("[1] somar")
   print("[2] multiplicar")
   print("[3] maior")
   print("[4] novos números")
   print("[5] sair do programa")
   print("="*20)
   resposta=int(input("qual é a sua opção? "))
   if resposta == 1:
         print("a soma entre {} e {} é {}".format(n1,n2,n1+n2))
   elif resposta == 2:
         print("a multiplicação entre {} e {} é {}".format(n1,n2,n1*n2))
   elif resposta == 3:
         print("o maior entre {} e {} é {}".format(n1,n2,max(n1,n2)))
   elif resposta == 4:
         continue
   elif resposta == 5:
         print("saindo do programa...")
         break
   else:
         print("opção inválida. tente novamente.")
