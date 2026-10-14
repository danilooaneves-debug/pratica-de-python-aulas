def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            return n
            break
        except ValueError:
            print("ERRO! Digite um número inteiro válido.")
       
           
n=leiaint("Digite um número: ")
print("Você digitou o número: ", n)
      