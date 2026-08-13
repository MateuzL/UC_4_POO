class Emprestimo:
    def __init__(self, codigo, pessoa, livro, dias, status):
        self.__codigo = ""
        self.__pessoa = ""
        self.__livro = ""
        self.__dias = ""
        self.__status = True

        self.set_codigo(codigo)
        self.set_pessoa(pessoa)
        self.set_livro(livro)
        self.set_dias(dias)
        self.set_status(status)


    #GET E SET CODIGO
    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        return self.__codigo

    #GET E SET PESSOA
    def get_pessoa(self):
        return self.__pessoa

    def set_pessoa(self, pessoa):
        return self.__pessoa

    #GET E SET LIVRO
    def get_livro(self):
        return self.__livro

    def set_livro(self, livro):
        return self.__livro

    #GET E SET DIAS
    def get_dias(self):
        return self.__dias

    def set_dias(self, dias):
        return self.__dias

    #GET E SET STATUS
    def get_status(self):
        return self.__status

    def set_status(self, status):
        return self.__status

    
    

    
'''
    def realizar(self):

    def finalizar(self):

    def calcular_multa(self):

    def exibir_resumo(self):'''