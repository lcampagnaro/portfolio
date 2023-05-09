def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if not formato else moeda(res)


def aumento(preço=1, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if not formato else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print(f'Resumo do Valor'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço é: \t{dobro(preço, True )}')
    print(f'Metade do preço é: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumento(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-'*30)