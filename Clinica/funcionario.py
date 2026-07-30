#Criar classe Funcionario

class Funcionario:
    def __init__(self, cargo, codigo, nome, crm, especialidade):
        self.cargo = cargo
        self.codigo = codigo
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade
        self.disponivel = True

    def exibir_dados(self):
        print("\n--- DADOS DO FUNCIONÁRIO ---")
        print(f"Cargo: {self.cargo}")
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"CRM: {self.crm}")
        print(f"Especialidade: {self.especialidade}")
        print(f"Disponibilidade: " f"{'Disponivel' if self.disponivel else 'Indisponivel'}")
