from produto import Produto

class Refeicao(Produto):

    def __init__(self, codigo, nome, preco, tamanho):
        super().__init__(codigo, nome, preco)
        self.tamanho = tamanho

    def get_preco(self):
        preco = super().get_preco()

        if self.tamanho.lower() == "grande":
            preco = preco * 1.20

        return preco

    def exibir_dados(self):
            print("\n--- REFEIÇÃO ---")
            super().exibir_dados()
            print(f"Volume: {self.tamanho}")
