from Ex115.lib.interface import *
from Ex115.arquivo import *
from time import sleep

arq = 'pacientes.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Pacientes', 'Novo Paciente', 'Sair do sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar nova pessoa
        cabeçalho('\33[35mNovo cadastro\33[m')
        nome = str(input('Nome do paciente: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Opção para sair do sistema
        cabeçalho('\33[36mSaindo do sistema... Até logo!\33[m')
        break
    else:
        print('\33[31mERRO: Digite uma opção válida!\33[m')
    sleep(2)
