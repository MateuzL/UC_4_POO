'''
Refeição - Se for do tamanho grande = acrescentar + 20% do valor

Bebida - volume = se bebida for acima de 500ml acrescentar valor de R$3,00

Sobremesa - se a sobremesa for especial = acrescentar +15%

'''
class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.__preco = 0.0

        self.set_preco(preco)

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco <= 0:
                    print("Erro: O preço deve ser maior que zero.")
                    return False
        self.__preco = float (preco)
        return True

    def calcular_preco(self, tamanho):
          if tamanho == "Grande":
                self.__preco = self.preco * 1.20

    def exibir_dados(self):
          print(f"Código: {self.codigo}")
          print(f"Nome: {self.nome}")
          print(f"Preço: R${self.__preco:.2f}")
