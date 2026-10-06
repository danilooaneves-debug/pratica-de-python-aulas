
def analisador(*num):
    maior = num[0]
    for n in num:
        if n > maior:
            maior = n
    print(f'{num}Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

analisador(2, 9, 4, 5, 7, 1)
    
