class PessoaFisica:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        f'{self.nome} - {self.dt_nascimento} - {self.endereco}'