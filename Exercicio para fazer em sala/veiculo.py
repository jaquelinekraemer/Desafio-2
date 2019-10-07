class Veiculo:
    def __init__(self, placa, ano, portas, cor, marca):
        self.placa = placa
        self.ano = ano
        self.portas = portas
        self.cor = cor
        self.marca = marca
    
    def __str__(self):
        return f'{super().__str__()} - {self.placa} - {self.ano} - {self.portas} - {self.cor} - {self.marca}'
