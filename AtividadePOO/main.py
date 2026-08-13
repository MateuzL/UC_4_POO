from pessoa import Pessoa
from aluno import Aluno
from professor import Professor
from livro import Livro

def main():
    aluno1 = Aluno(
        "Mateus",
        "12345678900",
        "12345",
        "Programação"
    )

    professor1 = Professor(
        "Luiz",
        "32165478977",
        "54321",
        "Tecnologia"
    )

    livro1 = Livro(
        "1",
        "Título",
        "Autor",
        ""
    )

    aluno1.exibir_dados()
    print()
    professor1.exibir_dados()
    print()
    livro1.exibir_dados()

main()




