# 07/10/2019

# Desafio de código PY004.
# Criar um programa que:
# 1. Leia os dados de um aluno: nome, sobrenome, idade e CPF.
# 2. Liste os dados de alunos cadastrados.
# 3. Ao cadastrar o sistema deve validar se já existe um aluno com o mesmo CPF e não deve
# permitir o cadastro, informando que o aluno já foi cadastrado.
# Obs: Utilizar aplicação consol, conceitos de dicionário e booleano vistos durante a semana.

def cria_cadastro(nome, sobrenome, idade, cpf):
    return{'nome': nome, 'sobrenome': sobrenome, 'idade': idade, 'cpf': cpf}

aluno = cria_cadastro('Luquinhas', 'Calminho', 12, '04487846487')

