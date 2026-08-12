class Aluguel:
    """
    Representa o relacionamento entre Cliente e Veiculo.

    A classe Aluguel não precisa saber se o veículo é
    Carro, Moto, Caminhonete ou Elétrico.

    Ela apenas chama calcular_aluguel().
    O próprio objeto decide qual regra executar.
    Isso evidencia o polimorfismo.
    """

    def __init__(self, codigo, cliente, veiculo, quantidade_dias):
        self.codigo = codigo
        self.cliente = cliente
        self.veiculo = veiculo
        self.quantidade_dias = quantidade_dias

        self.valor_total = 0.0
        self.status = "Pendente"

    def validar_aluguel(self):
        """Valida as regras básicas antes da locação."""
        if self.quantidade_dias <= 0:
            print("Erro: a quantidade de dias deve ser maior que zero.")
            return False

        if not self.veiculo.esta_disponivel():
            print("Erro: o veículo selecionado não está disponível.")
            return False

        return True

    def finalizar(self):
        """
        Finaliza o aluguel.

        Observe que a linha abaixo funciona com qualquer classe filha
        de Veiculo:
            self.veiculo.calcular_aluguel(...)
        """
        if self.status == "Finalizado":
            print("Este aluguel já foi finalizado.")
            return False

        if not self.validar_aluguel():
            return False

        # Polimorfismo em ação.
        self.valor_total = self.veiculo.calcular_aluguel(
            self.quantidade_dias
        )

        # O veículo passa a ficar indisponível.
        self.veiculo.alugar()

        self.status = "Finalizado"

        print("\nAluguel realizado com sucesso.")
        return True

    def exibir_resumo(self):
        """Exibe um resumo da locação."""
        print("\n================================")
        print("       RESUMO DO ALUGUEL")
        print("================================")
        print(f"Código do aluguel: {self.codigo}")
        print(f"Cliente: {self.cliente.get_nome()}")
        print(f"CPF: {self.cliente.get_cpf()}")
        print(
            f"Veículo: {self.veiculo.marca} "
            f"{self.veiculo.modelo}"
        )
        print(f"Quantidade de dias: {self.quantidade_dias}")
        print(f"Valor total: R$ {self.valor_total:.2f}")
        print(f"Status: {self.status}")
        print("================================")