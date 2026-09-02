class Reserva:

    def __init__(
        self,
        professor,
        sala,
        turma,
        data,
        horario
    ):
        self.professor = professor
        self.sala = sala
        self.turma = turma
        self.data = data
        self.horario = horario
        self.status = "Ativa"

    def criarReserva(self):

        self.status = "Ativa"

        print(
            "Reserva criada com sucesso!"
        )

    def cancelarReserva(self):

        if self.status == "Ativa":

            self.status = "Cancelada"

            print(
                "Reserva cancelada com sucesso!"
            )

        else:

            print(
                "Esta reserva não está ativa."
            )

    def alterarReserva(
        self,
        data,
        horario
    ):

        if self.status == "Ativa":

            self.data = data
            self.horario = horario

            print(
                "Reserva alterada com sucesso!"
            )

        else:

            print(
                "Não é possível alterar "
                "uma reserva cancelada."
            )

    def consultarReserva(self):

        print("\n--- RESERVA ---")

        print(
            f"Professor: "
            f"{self.professor.nome}"
        )

        print(
            f"Sala: "
            f"{self.sala.numero}"
        )

        print(
            f"Turma: "
            f"{self.turma.nome}"
        )

        print(
            f"Data: "
            f"{self.data}"
        )

        print(
            f"Horário: "
            f"{self.horario}"
        )

        print(
            f"Status: "
            f"{self.status}"
        )