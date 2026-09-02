class Reserva:

    def __init__(self, professor, sala, turma, data, horario):
        self.professor = professor
        self.sala = sala
        self.turma = turma
        self.data = data
        self.horario = horario
        self.status = "Ativa"

    def criarReserva(self):
        if self.sala.consultarDisponibilidade():
            self.sala.disponivel = False
            self.status = "Ativa"
            print("Reserva criada com sucesso!")
        else:
            print("A sala não está disponível.")

    def cancelarReserva(self):
        if self.status == "Ativa":
            self.status = "Cancelada"
            self.sala.disponivel = True
            print("Reserva cancelada com sucesso!")
        else:
            print("Esta reserva não está ativa.")

    def alterarReserva(self, data, horario):
        if self.status == "Ativa":
            self.data = data
            self.horario = horario
            print("Reserva alterada com sucesso!")
        else:
            print("Não é possível alterar uma reserva cancelada.")

    def consultarReserva(self):
        print("\n--- RESERVA ---")
        print(f"Professor: {self.professor.nome}")
        print(f"Sala: {self.sala.numero}")
        print(f"Turma: {self.turma.nome}")
        print(f"Data: {self.data}")
        print(f"Horário: {self.horario}")
        print(f"Status: {self.status}")