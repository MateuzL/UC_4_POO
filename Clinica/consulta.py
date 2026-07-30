class Consulta:
    def __init__(self, codigo, paciente, medico, data, horario):
        self.codigo = codigo
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.horario = horario
        self.status = "Agendada"

    def exibir_dados(self):
        print("\n--- DADOS DA CONSULTA ---")
        print(f"Código: {self.codigo}")
        print(f"Paciente: {self.paciente.nome}")
        print(f"Médico: {self.medico.nome}")
        print(f"Especialidade: {self.medico.especialidade}")
        print(f"Data: {self.data}")
        print(f"Horário: {self.horario}")
        print(f"Status: {self.status}")

    def validar_consulta(self):
        if not self.paciente.ativo:
            print("Consulta não pode ser agendada: Paciente inativo.")
            return False
        if not self.medico.disponivel:
            print("Consulta não pode ser agendada: Médico indisponivel.")
            return False
        print("Consulta validada com sucesso.")
        return True
    
    def confirmar_consulta(self):
        if self.status == "Cancelada":
            print("Não é possivel confirmar uma consulta cancelada.")
            return
        if self.status == "Realizada":
            print("A consulta já foi realizada.")
            return
        if self.validar_consulta():
            self.status = "Confirmada"
            self.medico.disponivel = False
            print("Consulta confirmada com sucesso.")
    
    def cancelar_consulta(self):
        if self.status == "Cancelada":
            print("A consulta já está cancelada.")
            return
        if self.status == "Realizada":
            print("Não é possivel cancelar uma consulta realizada.")
            return
        
        self.status = "Cancelada"
        self.medico.disponivel = True
        print("Consulta cancelada com sucesso.")

    def realizar_consulta(self):
        if self.status == "Cancelada":
            print("Não é possivel realizar uma consulta cancelada.")
            return
        if self.status == "Agendada":
            print("A consulta precisa ser confirmada antes.")
            return
        if self.status == "Realizada":
            print("A consulta já foi realizada.")
            return
        
        self.status = "Realizada"
        self.medico.disponivel = True
        print("Consulta realizada com sucesso.")
