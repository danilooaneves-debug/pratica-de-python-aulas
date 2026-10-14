def notas(*num, sit=False):
    nts = {}
    nts['total'] = len(num)
    nts['maior'] = max(num)
    nts['menor'] = min(num)
    nts['média'] = sum(num) / len(num)
    if sit:
        if nts['média'] >= 7:
            nts['situação'] = 'BOA'
        elif nts['média'] >= 5:
            nts['situação'] = 'RAZOÁVEL'
        else:
            nts['situação'] = 'RUIM'

    return nts

print(notas(5.5, 2.5, 9.5, sit=True))
