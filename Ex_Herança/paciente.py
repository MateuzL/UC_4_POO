from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco, idade, convenio):
        super().__init__(nome, cpf, telefone, endereco)

        self.idade = idade
        self.convenio = convenio

    def exibir_paciente(self):

        self.apresentar()
        print(f"Idade: {self.idade}")
        print(f"Convênio: {self.convenio}")
        