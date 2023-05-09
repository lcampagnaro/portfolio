from Ex111.utilidades import moeda
from Ex111.utilidades import dado

p = dado.leiaDinheiro('Digite um preço: R$')
ta = dado.leiaTaxa('Qual a taxa a ser trabalhada? ')
tr = ta
moeda.resumo(p, ta, tr)
