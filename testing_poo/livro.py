class Livro:
    def __init__(self, codigo, titulo, autor):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor

    def get_disponivel(self):
        return self.__disponivel

    def exibir_dados(self):
        print("=== DADOS DO LIVRO ===")
        print(f"Código: {self.__codigo}")
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Disponível: {'Sim' if self.__disponivel else 'Não'}")

    def emprestar(self):
        if not self.__disponivel:
            print("Erro: o livro já está emprestado.")
            return False

        self.__disponivel = False
        return True

    def devolver(self):
        self.__disponivel = True
