print("controle de terrenos")
print('=====================')

def terreno(larg, camp):
    area=larg * camp
    print(f"a área de {camp}x{larg} é {area} ")

q=float(input("LARGURA(m)"))
w=float(input("COMPRIMENTO(m)"))
terreno(q,w)