
resposta=0
c=1
n1=(int(input("digite o primeiro número da PA: ")))
r=(int(input("digite a razão da PA: ")))
while resposta != "N":
    print(n1, end=" ")
    n1 += r
    c += 1
    if c > 10:
        resposta = str(input("Deseja mostrar mais termos? [S/N] ")).upper()
        if resposta == "S":
            termos_a_mais = int(input("quantos termos você quer mostrar a mais? "))
            for _ in range(termos_a_mais-1):
                print(n1, end=" ")
                n1 += r
print("Fim")
