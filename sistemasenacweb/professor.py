from usuario import Usuario


class Professor(Usuario):

    def consultarSalas(self, salas):
        for sala in salas:
            print(
                f"Sala: {sala.numero} | "
                f"Capacidade: {sala.capacidade} | "
                f"Disponível: {sala.disponivel}"
            )

    def consultarReservas(self, reservas):
        for reserva in reservas:
            reserva.consultarReserva()

    def solicitarReserva(self, reserva):
        reserva.criarReserva()