'''Crie uma classe chamada carro, com os atributos marca, modelo, ano e velocidade.
A classe deve mostrar os métodos mostrar dados, acelerar e frear.

Regra:
O carro começa com a velocidade 0, ao acelerar, a velocidade aumenta 10, ao frear, a velocidade diminui 10.
A velocidade não pode ficar abaixo de 0.'''

class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self. velocidade = velocidade

    def mostrar_dados(self):
        print("Carro: ")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Velocidade: {self.velocidade}")

    def acelerar(self):
        self.velocidade = self.velocidade + 10

    def frear(self):
        if self.velocidade < 10:
            print("Velocidade não pode ser menor que 0")
        else:
            self.velocidade = self.velocidade - 10

        

carro1 = Carro("Volkswagen", "Tiguan R - line", 2015, 0)

carro1.mostrar_dados()

for i in range(3):
    carro1.acelerar()

carro1.mostrar_dados()

for j in range(3):
    carro1.frear()

carro1.mostrar_dados()

