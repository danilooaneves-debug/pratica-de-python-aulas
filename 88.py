import random
import time
print(30 * "=")
print("MEGA SENHA".center(30, "="))
print(30 * "=")
resp=int(input("quantos jogos vc quer jogar?"))
c=0
jogos=list()
while c < resp:
    jogo=random.sample(range(1, 61), 6)
    jogos.append(jogo)
    print(jogos)
    c += 1
    jogos.clear()
    time.sleep(0.5)


