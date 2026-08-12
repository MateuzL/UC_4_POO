from veiculo import Veiculo


class Caminhonete(Veiculo):
    """
    Classe filha de Veiculo.

    Regra de aluguel:
    - Valor das diárias
    - Acréscimo fixo de R$ 150,00 referente ao seguro
    """

    def __init__(
        self,
        codigo,
        marca,
        modelo,
        valor_diaria,
        capacidade_carga,
        quantidade_passageiros,
        tracao_4x4
    ):
        super().__init__(codigo, marca, modelo, valor_diaria)

        self.capacidade_carga = capacidade_carga
        self.quantidade_passageiros = quantidade_passageiros
        self.tracao_4x4 = tracao_4x4

    def calcular_aluguel(self, quantidade_dias):
        """Aplica a taxa fixa de seguro."""
        if quantidade_dias <= 0:
            return 0

        valor = self.get_valor_diaria() * quantidade_dias
        taxa_seguro = 150.00

        return valor + taxa_seguro

    def exibir_dados(self):
        print("\n--- CAMINHONETE ---")
        super().exibir_dados()
        print(f"Capacidade de carga: {self.capacidade_carga} kg")
        print(f"Passageiros: {self.quantidade_passageiros}")
        print(f"Tração 4x4: {'Sim' if self.tracao_4x4 else 'Não'}")