from produto import Produto

class Bebida(Produto):
    def __init__(self, codigo, nome, preco, volume):
        super().__init__(codigo, nome, preco)

        self.volume = volume

    def calcular_preco(self, tamanho):
        return super().calcular_preco(tamanho)

    def exibir_dados(self):
        print("\n--- BEBIDA ---")
        super().exibir_dados()
        print(f"Volume: {self.volume}")