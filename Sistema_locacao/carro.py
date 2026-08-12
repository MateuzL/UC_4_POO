from veiculo import Veiculo


class Carro(Veiculo):
    """
    Classe filha de Veiculo.

    Regra de aluguel:
    - Até 10 dias: valor normal.
    - Acima de 10 dias: 5% de desconto.
    """

    def __init__(self, codigo, marca, modelo, valor_diaria, quantidade_portas):
        # super() chama o construtor da classe-pai Veiculo.
        super().__init__(codigo, marca, modelo, valor_diaria)

        self.quantidade_portas = quantidade_portas

    def calcular_aluguel(self, quantidade_dias):
        """
        Sobrescreve o método da classe Veiculo.
        Isso é um exemplo de polimorfismo.
        """
        if quantidade_dias <= 0:
            return 0

        valor = self.get_valor_diaria() * quantidade_dias

        # Regra específica do carro.
        if quantidade_dias > 10:
            valor *= 0.95  # desconto de 5%

        return valor

    def exibir_dados(self):
        """
        Reaproveita os dados da classe-pai e adiciona
        a quantidade de portas.
        """
        print("\n--- CARRO ---")
        super().exibir_dados()
        print(f"Portas: {self.quantidade_portas}")