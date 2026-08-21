from produto import Produto

class Sobremesa(Produto):
    def __init__(self, codigo, nome, preco, especial):
        super().__init__(codigo, nome, preco)

        self.especial = especial

    def get_preco(self):
        preco = super().get_preco()

        if self.especial:
            preco = preco * 1.15
        return preco

    def exibir_dados(self):
        print(f"\n--- SOBREMESA ---")
        super().exibir_dados()
        #print(f"Especial: {self.especial}")


        