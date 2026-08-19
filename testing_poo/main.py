from aluno import Aluno
from professor import Professor
from livro import Livro
from emprestimo import Emprestimo


# Criando pessoas
aluno = Aluno(
    "Mateus",
    "123.456.789-00",
    "2026001",
    "Desenvolvimento de Sistemas"
)

professor = Professor(
    "Carlos",
    "987.654.321-00",
    "PROF001",
    "Tecnologia da Informação"
)


# Criando livros
livro1 = Livro(
    1,
    "Python para Iniciantes",
    "Gustavo Guanabara"
)

livro2 = Livro(
    2,
    "Introdução à Programação",
    "Autor Exemplo"
)


# Polimorfismo
print("========== PESSOAS ==========")

pessoas = [aluno, professor]

for pessoa in pessoas:
    pessoa.exibir_dados()
    print()


# Exibindo livros
print("========== LIVROS ==========")

livro1.exibir_dados()
print()

livro2.exibir_dados()


# Primeiro empréstimo
print("\n========== PRIMEIRO EMPRÉSTIMO ==========")

emprestimo1 = Emprestimo(
    1,
    aluno,
    livro1,
    10
)

emprestimo1.realizar()
emprestimo1.exibir_resumo()


# Tentativa de emprestar livro indisponível
print("\n========== SEGUNDO EMPRÉSTIMO ==========")

emprestimo2 = Emprestimo(
    2,
    professor,
    livro1,
    5
)

emprestimo2.realizar()


# Finalizando primeiro empréstimo
print("\n========== FINALIZANDO PRIMEIRO EMPRÉSTIMO ==========")

emprestimo1.finalizar()
emprestimo1.exibir_resumo()


# Livro pode ser emprestado novamente
print("\n========== NOVO EMPRÉSTIMO ==========")

emprestimo2.realizar()
emprestimo2.exibir_resumo()
