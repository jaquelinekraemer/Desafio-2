from veiculo import Veiculo

class Jetski(Veiculo):
    def __init__(self, ano, cor, modelo, marca):
        super().__init__(ano, cor, marca)
        self.modelo = modelo
