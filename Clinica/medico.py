class Medico:
    def __init__(self, codigo, nome, crm, especialidade):
        self.codigo = codigo
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade
        self.disponivel = True

    def exibir_dados(self):
        print("\n--- DADOS DO MÉDICO ---")
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"CRM: {self.crm}")
        print(f"Especialidade: {self.especialidade}")
        print(f"Disponibilidade: " f"{'Disponivel' if self.disponivel else 'Indisponivel'}")
    
    def alterar_disponibilidade(self):
        self.disponivel = not self.disponivel

        if self.disponivel:
            print(f"Medico {self.nome} agora está disponivel.")
        else:
            print(f"Médico {self.nome} agora está indisponivel.")
