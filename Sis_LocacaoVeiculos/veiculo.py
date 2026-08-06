class Veiculo:
    def __init__(self, codigo, marca, modelo, valor_diaria):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo
        self.__valor_diaria = 0.0
        self.__disponivel = True

        self.set_valor_diaria(valor_diaria)


    def get_valor_diaria(self):
        return self.__valor_diaria


    def set_valor_diaria(self, valor):
        if valor < 0:
            print("Erro: O valor da diária deve se maior que zero!")
            return False

        self.__valor_diaria = valor
        return True


    def esta_disponivel(self):
        return self.__disponivel


    def alugar(self):
        if not self.__disponivel:
            print("O Veículo já está alugado.")
            return False

        self.__disponivel = False
        return True


    def devolver(self):
        if self.__disponivel:
            print("O Veículo já está disponível.")
            return False
        
        self.__disponivel = True
        print("Veículo devolvido com sucesso.")
        return True

    
    def calcular_aluguel(self, quantidade_dias):
        if quantidade_dias <= 0:
            return 0

        return self.__valor_diaria * quantidade_dias


    def exibir_dados(self):
        situacao = "Disponível" if self.__disponivel else "Alugado"

        print(f"Código: {self.codigo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Diária: R$ {self.__valor_diaria:.2f}")
        print(f"Situação: {situacao}")
