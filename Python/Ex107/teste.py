import moeda

p = float(input('Digite um número: '))
t = float(input('Tem taxa para acrescentar ou descontar? Digite a %: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.')
print(f'Com o aumento de {moeda.taxa(t)} o preço vale {moeda.aumento(p, t, True)}.')
print(f'Se diminuir {moeda.taxa(t)} o preço fica {moeda.diminuir(p, t, True)}.')