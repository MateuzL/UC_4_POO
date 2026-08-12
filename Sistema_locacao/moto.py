from veiculo import Veiculo


class Moto(Veiculo):
    """
    Classe filha de Veiculo.

    Regra de aluguel:
    - Até 5 dias: valor normal.
    - Acima de 5 dias: 10% de desconto.
    """

    def __init__(self, codigo, marca, modelo, valor_diaria, cilindrada):
        super().__init__(codigo, marca, modelo, valor_diaria)

        self.cilindrada = cilindrada

    def calcular_aluguel(self, quantidade_dias):
        """
        Sobrescreve calcular_aluguel() da classe-pai.
        """
        if quantidade_dias <= 0:
            return 0

        valor = self.get_valor_diaria() * quantidade_dias

        if quantidade_dias > 5:
            valor *= 0.90  # desconto de 10%

        return valor

    def exibir_dados(self):
        print("\n--- MOTO ---")
        super().exibir_dados()
        print(f"Cilindrada: {self.cilindrada} cc")