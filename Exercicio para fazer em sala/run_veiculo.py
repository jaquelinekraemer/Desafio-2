from veiculo import Veiculo
from moto import Moto
from jetski import Jetski

lista = []
opcao = 5

def monta_menu():
print("="*50)
print('0-Sair')
print('1-Cadastrar Veiculo')
print('2-Cadastrar Moto')
print('3-Cadastrar Jetski')
print('4-Listar')
print("="*50)

def cadastra_veiculo():
print("Cadastre seu veiculo")
placa = input('Placa:')
        ano = input('Ano:')
        portas = input('Número de Portas:')
        cor = input('Cor:')
        marca = input('Marca:')
        return Veiculo(placa, ano, portas, cor, marca)

    def cadastra_moto():
        print("Informe os dados da sua moto")
        placa = input('Placa:')
        ano = input('Ano:')
        cor = input('Cor:')
        marca = input('Marca:')
        km = input('Km:')
        return Moto(placa, ano, cor, marca, km)

    def cadastra_jetski():
        print("Informe os dados do seu jetski")
        ano = input('Ano:')
        cor = input('Cor:')
        modelo = input('Modelo:')
        marca = input('Marca:')
        return Moto(placa, ano, cor, marca, km)

    def lista():
        print("Lista")
        for p in lista:
            print(p)