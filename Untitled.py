valor=int(input("qual é o valor da casa(R$): "))
salario=int(input("qual é o seu salário(R$): "))
anos=int(input("em quantos anos você quer pagar? "))
prestacao=valor/(anos*12)
print("a prestação será de R${:.2f}".format(prestacao))
if prestacao>salario*0.3:
    print("empréstimo negado")
else:
    print("empréstimo aprovado")

