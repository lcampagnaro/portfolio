listagem = ('Lápis', 2.75,
            'Borracha', 2,
            'Caderno', 16.99,
            'Caneta', 5.49,
            'Régua', 7.50,
            'Compasso', 18.99,
            'Estojo', 25,
            'Livro', 135.9,
            )
print('-' * 41)
print(f'{"Listagem de Preços": ^41}')
print('-' * 41)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f' {listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f} ')
print('-' * 41)