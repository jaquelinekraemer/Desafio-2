from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, placa, ano, cor, marca, km):
        super().__init__(placa, ano, cor, marca)
        self.km = km
