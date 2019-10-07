# Criar um programa que cadastra pessoas físicas e jurídicas
# 1. Solicite qual o tipo de pessoa que o usuário deseja cadastrar.
# 2. Solicite os dados de acordo com o tipo de pessoa selecionada.
# 3. Liste todas as pessoas cadastradas em uma única página.
# Obs: O programa deve ser feito para aplicativo console e deve utilizar o conceito de classes. O
# cadastro deve possuir no mínimo nome completo e Documento principal de acordo com o tipo
# (CPF, CNPJ).

from pf import PessoaFisica
from pj import PessoaJuridica


def monta_menu():
    print("="*50)
    print('0-Sair')
    print('1-Cadastrar PF')
    print('2-Cadastrar PJ')
    print('3-Listar Cadastro')
    print("="*50)

def cadastra_pf():
    print("PF")
    nome = input('Nome:')
    cpf = input('CPF:')
    return PessoaFisica(nome, cpf)

def cadastra_pj():
    print("PJ")
    nome = input('Nome:')
    cnpj = input('CNPJ:')
    return PessoaJuridica(nome, cnpj)

def lista():
    print("Lista")
    for p in lista:
        print(p)

lista = []
opcao = 4

while opcao != 0:
    monta_menu()
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        lista.append(cadastra_pf())
    elif opcao == 2:
        lista.append(cadastra_pj())
    elif opcao == 3:
        lista()

