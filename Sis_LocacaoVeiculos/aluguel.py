class Aluguel:
    def __init__(self, codigo, cliente, veiculo, quantidade_dias):
        self.codigo = codigo
        self.cliente = cliente
        self.veiculo = veiculo
        self.quantidade_dias = quantidade_dias

        self.valor_total = 0.0
        self.status = "Pendente"

    def validar_aluguel(self):
        if self.quantidade_dias <= 0:
            print("Erro: A quantidade de dias deve ser maior que zero.")
            return False
        
        if not self.veiculo.esta_disponivel():
            print("Erro: O Veículo selecionado não está disponível.")
            return False
        return True

    def finalizar(self):
        if self.status == "Finalizado":
            print("Este Aluguel já foi finalizado.")
            return False

        self.valor_total = self.veiculo.calcular_aluguel(self.quantidade_dias)

        self.veiculo.alugar()

        self.status = "Finalizado"

        print("\n Aluguel realizado com sucesso!")
        return True

    def exibir_resumo(self):
        print("\n --- RESUMO DO ALUGUEL ---")
        print(f"Código do aluguel: {self.codigo}")
        print(f"Cliente: {self.cliente.get_nome()}")
        print(f"CPF: {self.cliente.get_cpf()}")
        print(f"Veículo: {self.veiculo.marca}" f"{self.veiculo.modelo}")
        print(f"Quantidade de dias: {self.quantidade_dias}")
        print(f"Valor Total: R$ {self.valor_total:.2f}")
        print(f"Status: {self.status}")