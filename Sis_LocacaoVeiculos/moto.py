from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, codigo, marca, modelo, valor_diaria, cilindrada):
        super().__init__(codigo, marca, modelo, valor_diaria)
        self.cilindrada = cilindrada

    def exibir_moto(self):
        print("\n--- MOTO ---")
        self.exibir_dados()
        print(f"Cilindradas: {self.cilindrada}")