from usuario import Usuario


class Coordenador(Usuario):

    def cadastrarSala(self, sala):
        sala.cadastrar()

    def alterarSala(self, sala, capacidade):
        sala.alterar(capacidade)

    def excluirSala(self, sala):
        sala.excluir()

    def consultarSalas(self, salas):
        for sala in salas:
            print(
                f"Sala: {sala.numero} | "
                f"Capacidade: {sala.capacidade} | "
                f"Disponível: {sala.disponivel}"
            )