from produto import Produto

class Refeicao(Produto):
    def __init__(self, codigo, nome, preco, tamanho):
        super().__init__(codigo, nome, preco)

        self.tamanho = tamanho


    def calcular_preco(self, tamanho):
        if tamanho == "Grande":
            valor = self.__preco * 1.20

        return self.__preco == valor

    def exibir_dados(self):
        print("\n--- DADOS REFEIÇÃO ---")
        super().exibir_dados()
        print(f"Tamanho: {self.tamanho}")