class Usuario:
    def __init__(self, nome, email, telefone, senha, cargo):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.cargo = cargo

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}.")
        print(f"Meu email é: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Senha: {self.senha}")
        print(f"Cargo: {self.cargo}")

usuario1 = Usuario("João", "joao@outlook.com", 67998784565, "Senha123", "Professor")

usuario1.apresentar()


class Progresso:
    def __init__(self, data, aguaConsumida, pausasRealizadas, alongamentosFeitos):
        self.data = data
        self.aguaConsumida = aguaConsumida
        self.pausasRealizadas = pausasRealizadas
        self.alongamentosFeitos = alongamentosFeitos

    def apresentar(self):
        print(f"Data: {self.data}")
        print(f"Água consumida: {self.aguaConsumida}")
        print(f"Pausas Realizadas: {self.pausasRealizadas}")
        print(f"Alongamentos realizados: {self.alongamentosFeitos}")


