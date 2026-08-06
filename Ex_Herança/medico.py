from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco, crm, especialidade):
        super().__init__(nome, cpf, telefone, endereco)

        self.crm = crm
        self.especialidade = especialidade

    def exibir_medico(self):

        self.apresentar()
        print(f"Crm: {self.crm}")
        print(f"Especialidade: {self.especialidade}")