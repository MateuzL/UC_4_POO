class Veiculo:
    def __init__(self, tipo, marca, modelo, ano):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def apresentar(self):
        print("--- VEÍCULO ---")
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")