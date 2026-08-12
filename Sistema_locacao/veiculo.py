class Veiculo:
    """
    Classe-pai de todos os veículos da locadora.

    Conceitos trabalhados:
    - Herança
    - Encapsulamento
    - Métodos
    - Regras de negócio
    - Polimorfismo
    """

    def __init__(self, codigo, marca, modelo, valor_diaria):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo

        # A diária é privada porque não queremos aceitar valores inválidos.
        self.__valor_diaria = 0.0

        # Todo veículo inicia disponível para locação.
        self.__disponivel = True

        self.set_valor_diaria(valor_diaria)

    def get_valor_diaria(self):
        """Retorna o valor atual da diária."""
        return self.__valor_diaria

    def set_valor_diaria(self, valor):
        """Altera o valor da diária somente se o valor for válido."""
        if valor <= 0:
            print("Erro: o valor da diária deve ser maior que zero.")
            return False

        self.__valor_diaria = float(valor)
        return True

    def esta_disponivel(self):
        """Retorna True quando o veículo estiver disponível."""
        return self.__disponivel

    def alugar(self):
        """
        Marca o veículo como alugado.
        Não permite alugar um veículo que já está indisponível.
        """
        if not self.__disponivel:
            print("O veículo já está alugado.")
            return False

        self.__disponivel = False
        return True

    def devolver(self):
        """
        Libera o veículo para uma nova locação.
        """
        if self.__disponivel:
            print("O veículo já está disponível.")
            return False

        self.__disponivel = True
        print("Veículo devolvido com sucesso.")
        return True

    def calcular_aluguel(self, quantidade_dias):
        """
        Regra padrão de cálculo.

        As classes filhas podem sobrescrever este método,
        caracterizando polimorfismo.
        """
        if quantidade_dias <= 0:
            return 0

        return self.__valor_diaria * quantidade_dias

    def exibir_dados(self):
        """Exibe os dados comuns a todos os veículos."""
        situacao = "Disponível" if self.__disponivel else "Alugado"

        print(f"Código: {self.codigo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Diária: R$ {self.__valor_diaria:.2f}")
        print(f"Situação: {situacao}")
        