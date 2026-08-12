from veiculo import Veiculo


class Eletrico(Veiculo):
    """
    Veículo elétrico.

    Regra de aluguel:
    - 15% de desconto ecológico em qualquer locação.
    """

    def __init__(
        self,
        codigo,
        marca,
        modelo,
        valor_diaria,
        autonomia,
        tempo_recarga
    ):
        super().__init__(codigo, marca, modelo, valor_diaria)

        self.autonomia = autonomia
        self.tempo_recarga = tempo_recarga

    def calcular_aluguel(self, quantidade_dias):
        """
        Polimorfismo:
        mesma assinatura do método, mas com regra própria.
        """
        if quantidade_dias <= 0:
            return 0

        valor = self.get_valor_diaria() * quantidade_dias

        return valor * 0.85  # desconto de 15%

    def exibir_dados(self):
        print("\n--- VEÍCULO ELÉTRICO ---")
        super().exibir_dados()
        print(f"Autonomia: {self.autonomia} km")
        print(f"Tempo de recarga: {self.tempo_recarga} h")