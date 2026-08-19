class Emprestimo:
    def __init__(self, codigo, pessoa, livro, dias):
        self.__codigo = codigo
        self.__pessoa = pessoa
        self.__livro = livro
        self.__dias = dias
        self.__status = "Pendente"

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_pessoa(self):
        return self.__pessoa

    def set_pessoa(self, pessoa):
        self.__pessoa = pessoa

    def get_livro(self):
        return self.__livro

    def set_livro(self, livro):
        self.__livro = livro

    def get_dias(self):
        return self.__dias

    def set_dias(self, dias):
        self.__dias = dias

    def get_status(self):
        return self.__status

    def realizar(self):
        if self.__status != "Pendente":
            print("Erro: este empréstimo já foi realizado ou finalizado.")
            return False

        if self.__dias <= 0:
            print("Erro: a quantidade de dias deve ser maior que zero.")
            return False

        if not self.__livro.emprestar():
            return False

        self.__status = "Em andamento"
        print("Empréstimo realizado com sucesso!")
        return True

    def finalizar(self):
        if self.__status != "Em andamento":
            print("Erro: não existe um empréstimo em andamento.")
            return False

        self.__livro.devolver()
        self.__status = "Finalizado"
        print("Empréstimo finalizado com sucesso!")
        return True

    def calcular_multa(self):
        if self.__dias <= 7:
            return 0.0

        dias_excedentes = self.__dias - 7
        return dias_excedentes * 2.00

    def exibir_resumo(self):
        print("\n=== RESUMO DO EMPRÉSTIMO ===")
        print(f"Código: {self.__codigo}")
        print(f"Pessoa: {self.__pessoa.get_nome()}")
        print(f"Livro: {self.__livro.get_titulo()}")
        print(f"Dias: {self.__dias}")
        print(f"Status: {self.__status}")
        print(f"Multa: R$ {self.calcular_multa():.2f}")
