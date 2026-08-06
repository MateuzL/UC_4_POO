class Teste:   #encapsulamento 
    def __init__(self, valor):
        self.x = valor   

    def get_valor(self):
        return self.x

    def set_valor(self, v):
        self.x = v 

teste = Teste(10)
print(" O valor do Objeto: ", teste.get_valor())

val = int(input("Digite um novo valor: "))
teste.set_valor(val)
print("O novo valor  do objeto: ", teste.get_valor())