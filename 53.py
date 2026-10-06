frase=str(input("digite uma frase: ")).strip().lower().split
if frase==frase[::-1]:
    print("essa frase é um palíndromo")
else:
    print("essa frase não é um palíndromo")


