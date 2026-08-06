from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, tipo, marca, modelo, ano, cor, cambio):
        super().__init__(tipo, marca, modelo, ano)

        self.cor = cor
        self.cambio = cambio

    def exibir_carro(self):

        self.apresentar()
        print(f"Cor: {self.cor}")
        print(f"Cambio: {self.cambio}")