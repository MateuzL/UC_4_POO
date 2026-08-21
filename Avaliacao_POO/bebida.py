from produto import Produto

class Bebida(Produto):
    def __init__(self, codigo, nome, preco, volume):
        super().__init__(codigo, nome, preco)

        self.volume = volume

    def get_preco(self):
        preco = super().get_preco()

        if self.volume > 500:
            preco = preco + 3.00
        return preco

    def exibir_dados(self):
        print("\n--- BEBIDA ---")
        super().exibir_dados()
        #print(f"Volume: {self.volume}")

