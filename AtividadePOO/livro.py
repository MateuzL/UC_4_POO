class Livro:
    def __init__(self, codigo, titulo, autor, disponivel):
        self.__codigo = ""
        self.__titulo = ""
        self.__autor = ""
        self.__disponivel = True

        self.set_codigo(codigo)
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_disponivel(disponivel)

    #GET E SET CODIGO
    def get_codigo(self):
        return self.__codigo
    def set_codigo(self, codigo):
        self.__codigo = codigo
        return True

    #GET E SET TITULO
    def get_titulo(self):
        return self.__titulo
    def set_titulo(self, titulo):
        self.__titulo = titulo
        return True

    #GET E SET AUTOR
    def get_autor(self):
        return self.__autor
    def set_autor(self, autor):
        self.__autor = autor
        return True

    #GET E SET DISPONIVEL
    def get_disponivel(self):
        return self.__disponivel
    def set_disponivel(self, disponivel):
        return self.__disponivel

    def exibir_dados(self):
        print("--- DADOS LIVRO ---")
        print(f"Código: {self.get_codigo()}")
        print(f"Título: {self.get_titulo()}")
        print(f"Autor: {self.get_autor()}")
        print(f"Disponível: {self.get_disponivel()}")

'''
    def emprestar(self):

    def devolver(self):'''
    
