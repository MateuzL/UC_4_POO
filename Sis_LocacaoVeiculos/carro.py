from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, codigo, marca, modelo, valor_diaria, quantidade_portas):
        super().__init__(codigo, marca, modelo, valor_diaria)

        self.quantidade_portas = quantidade_portas

    def exibir_carro(self):
        print("\n--- CARRO ---")
        self.exibir_dados()
        print(f"Quantidade de portas: {self.quantidade_portas}")