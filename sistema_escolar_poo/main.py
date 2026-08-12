from aluno import Aluno
from professor import Professor
from escola import Escola


def main():
    escola = Escola("Escola Senac")

    aluno = Aluno("Eduardo", 20, "2026001")
    aluno.adicionar_nota(8)
    aluno.adicionar_nota(7)
    aluno.adicionar_nota(9)

    professor = Professor("Luiz", 35, "Programação", 3500)

    escola.adicionar_aluno(aluno)
    escola.adicionar_professor(professor)

    print("=" * 50)
    print(f"ESCOLA: {escola.get_nome()}")
    print("=" * 50)

    print("\n--- ALUNO ---")
    print(aluno.apresentar())
    print(f"Matrícula: {aluno.get_matricula()}")
    print(f"Notas: {aluno.get_notas()}")
    print(f"Média: {aluno.calcular_media():.2f}")
    print(f"Situação: {aluno.verificar_aprovacao()}")

    print("\n--- PROFESSOR ---")
    print(professor.exibir_informacoes())
    print(professor.ministrar_aula())

    print("\n--- PESSOAS CADASTRADAS ---")
    for pessoa in escola.listar_pessoas():
        print(pessoa)

    print("\n--- TESTE DE HERANÇA ---")
    print(f"Tipo do aluno: {aluno.exibir_tipo()}")
    print(f"Tipo do professor: {professor.exibir_tipo()}")

    print("\n--- TESTE DE SETTERS ---")
    aluno.set_nome("Luiz")
    professor.set_nome("Eduardo")
    professor.set_disciplina("Desenvolvimento de Sistemas")
    print(aluno.apresentar())
    print(professor.exibir_informacoes())


if __name__ == "__main__":
    main()
