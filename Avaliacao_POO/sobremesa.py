from produto import Produto

class Sobremesa(Produto):
    def __init__(self, codigo, nome, preco, especial):
        super().__init__(codigo, nome, preco)

        self.especial = especial

    def calcular_preco(self, tamanho):
        return super().calcular_preco(tamanho)

    def exibir_dados(self):
        print(f"\n--- SOBREMESA ---")
        super().exibir_dados()
        print(f"Especial: {self.especial}")
        
        